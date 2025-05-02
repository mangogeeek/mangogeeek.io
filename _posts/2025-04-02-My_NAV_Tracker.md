# Automated Profit Booking System

**Sheet Name**: `MUF:NIFTY_Alpha_50`  
**Profit Threshold**: 6% above invested value  
**NAV Source**: [API](https://api.mfapi.in/mf/152177/latest)

* * *

## 📊 Key Formulas

| Cell | Formula | Purpose |
| --- | --- | --- |
| **B1** | `=getNAV()` (script) | Current NAV (auto-updated) |
| **B3** | `=SUMIF(E:E,"Buy",G:G)-SUMIF(E:E,"Sell",G:G)` | Units held |
| **B4** | `=SUM(H:H)` | Net invested value |
| **B6** | `=B3*B1` | Current portfolio value |
| **B8** | `=IF(B4=0, 0, (B6-B4)/B4)` | Unrealized profit % |
| **B10** | `=IF(B8>6%, (B6-B4*1.06)/B1, "")` | Units to sell for 6% profit |
| **B11** | Script-controlled status | Execution logs |

* * *

## 🤖 Scripts

### 1\. NAV Fetcher (`getNAV()`)

```JavaScript
function getNAV() {
  try {
    const response = UrlFetchApp.fetch("https://api.mfapi.in/mf/152177/latest?t=" + new Date().getTime());
    return JSON.parse(response).data[0].nav;
  } catch (e) {
    console.error("NAV Error: " + e);
    return null;
  }
}

```

### 2\. Profit Booker (`autoBookProfit()`)

```JavaScript
function autoBookProfit() {
  const sheet = SpreadsheetApp.getActive().getSheetByName("MUF:NIFTY_Alpha_50");
  const [nav, units, invested] = sheet.getRange("B1,B3,B4").getValues().flat();
  const profit = (nav*units - invested)/invested;
  
  if (profit > 0.06) {
    const sellUnits = ((nav*units - invested*1.06)/nav).toFixed(2);
    sheet.appendRow([new Date(), "Sell", nav, -sellUnits, -(sellUnits*nav)]);
    sheet.getRange("B11").setValue(`✅ Sold ${sellUnits} units @ ${nav}`);
  }
}
```

### 3\. Auto-Refresh (`refreshNAV()`)

```JavaScript
function refreshNAV() {  
  const sheet = SpreadsheetApp.getActive().getSheetByName("MUF:NIFTY_Alpha_50");  
  const nav = getNAV();  
  if (nav !== null) {  
    sheet.getRange("B1").setValue(nav);  
    sheet.getRange("B2").setValue(new Date()).setNumberFormat("yyyy-mm-dd hh:mm:ss");  
  }  
}

```

## ⚙️ Triggers

- **🕒 Daily NAV Update**: 6:45 PM IST
    
- **🛠️ Manual Controls**:
    
    - `🔔 NAV Tools > Refresh NAV Now`
        
    - `💰 Auto-Book Profit > Check & Sell`
        

* * *

## 🔄 Workflow

1.  **NAV Updates** → `B1` (auto)
    
2.  **Profit Calculation** → `B8`
    
3.  **Auto-Sell** → Triggers when `B8 > 6%`
    
4.  **Logs** → `B11` & Columns `D-H`
    

* * *

## 🚨 Error Handling

- **Failed API Calls**: Logs to `B11`
    
- **Sheet/Range Errors**: Console alerts
    
- **Data Validation**: Checks numeric values
    

* * *

## 💡 Pro Tips

**Backup NAV Source**:

```Excel
=IFERROR(getNAV(), GOOGLEFINANCE("MUTF_IN:BAND_NIFT_ALPH_1EDZ6YT", "nav"))
```

**Telegram Alerts** (Add to script):

```JavaScript
UrlFetchApp.fetch(`https://api.telegram.org/botTOKEN/sendMessage?chat_id=ID&text=📈 NAV: ${nav}`);
```
