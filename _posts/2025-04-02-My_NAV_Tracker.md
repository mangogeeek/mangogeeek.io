# Profit Booking System Analysis

**Sheet Link**: [MUF:NIFTY_Alpha_50](https://docs.google.com/spreadsheets/d/1DigvSVPG7mlkDYYarR03dAUys00Zd-sgA3cWXXwEHTU/edit#gid=403913121)

## 🔍 Core Methodology

### 1\. Fundamental Formulas

`Profit % = (Current Value - Invested Value) / Invested Value`

Where:

**Current Value =** `Units × Current NAV (B3 × B1)`

**Invested Value =** `Total Buy Amounts - (Units Sold × Average Buy NAV)`

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

2.  Key Components
    

| Cell | Formula | Purpose |
| --- | --- | --- |
| B4  | `=SUMIF(E:E,"Buy",H:H)-SUMIF(E:E,"Sell",G:G)*B5` | True invested value |
| B10 | `=IF(B8>6%,(B6-B4)/B1,"None")` | Units to sell |

2.  ## 📊 How It Works
    
    ### Transaction Flow
    
      
    <br/>
    
    ```mermaid
    graph TD
        A[Buy Transaction] --> B[Increase Invested Value]
        C[Sell Transaction] --> D[Reduce Invested Value by Cost Basis]
        B --> E[Update Avg NAV]
        D --> E
        E --> F[Calculate Profit%]
        F --> G{Profit >6%?}
        G -->|Yes| H[Sell Units]
        G -->|No| I[Monitor]
        H --> D
    
    ```
    

* * *

### Mathematical Proof

To reset profit to 0%:

```
Units to Sell = (Current Value - Invested Value) / Current NAV
```

**Example**:

- Current Value = ₹4,146,512
    
- Invested Value = ₹3,781,935
    
- NAV = ₹14
    
- Units to Sell = `(4,146,512 - 3,781,935)/14 = 26,041 units`
    

## 💡 Key Insights

1.  **Cost Basis Isolation**
    
    - Uses original purchase price (Avg NAV) for sold units
        
    - Not affected by current NAV fluctuations
        
2.  **Full Position Exit**
    
    - Only complete sale resets profit to 0%
        
    - Partial sales maintain proportional profit
        
3.  **Self-Consistent System**
    
    - No circular references
        
    - All values update atomically
        

## ⚙️ Implementation Guide

### 1\. Setup Required

- **Column D-H**: Record all transactions
    
- **Formulas**: Implement in Column B as shown above
    
- **Formatting**:
    
```Excel
Conditional Formatting:
- B8 >6% → Yellow
- B10 ≠ "None" → Green
```

### 2\. Automation Script

```JavaScript
function autoBookProfit() {
  const sheet = SpreadsheetApp.getActive().getSheetByName("MUF:NIFTY_Alpha_50");
  const [nav, units, invested] = sheet.getRange("B1,B3,B4").getValues().flat();
  const profit = (nav*units - invested)/invested;

  if (profit > 0.06) {
    const sellUnits = ((nav*units - invested)/nav).toFixed(2);
    sheet.appendRow([
      new Date(), 
      "Sell", 
      nav, 
      -sellUnits, 
      -(sellUnits*nav)
    ]);
  }
}
```
