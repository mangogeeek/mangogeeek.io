# Atlassian Projects ecosystem

## Support Project Types

| ***Product Name*** | ***Project Type*** | ***Unique Issue Types*** | ***Standard Issue Types*** | ***Management Type*** |
| --- | --- | --- | --- | --- |
| ***Jira Product Discovery*** | *Product Discovery* | *Ideas* | *Task, Sub-task* | *Team-managed only* |
| ***Jira Service Management*** | *Service Management* | *Request, Incident, Problem, Change, Service Request* | *Task, Sub-task, Custom Request Types* | *Company and Team-managed* |
| ***Jira*** | *Software Projects* | *Epic, Story, Bug* | *Task, Sub-task* | *Company and Team-managed* |
| ***Jira Work Management*** | *Business Projects* | *None* | *Task, Sub-task* | *Company and Team-managed* |

---

## Workflow Representation of JIRA Elements

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXcAa5PS39fOC5SH-SCbWTjSUte2ZQUUP4fTzjOTyO1RGOh2w-c34MHfNBP_YMoyb9kmal-AyhOxPBErNfmS6eGnSKK92fWd0w_Sv-35VHB1DsKpPRp7SE0Ql7poTv_7NVBSa086IA?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcAa5PS39fOC5SH-SCbWTjSUte2ZQUUP4fTzjOTyO1RGOh2w-c34MHfNBP_YMoyb9kmal-AyhOxPBErNfmS6eGnSKK92fWd0w_Sv-35VHB1DsKpPRp7SE0Ql7poTv_7NVBSa086IA?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

## Comprehensive Guide to JIRA Project Creation and Modification (Example-Based Learning)

Let’s set up a company managed Jira project for a software development team. The goal is to manage (**Bugs** and **Tasks) Issue Types** , ensuring that issues move through their respective workflows, fields are configured correctly, and notifications reach the right people.

- **Setup Objective**: Configure schemes for **Issue Types**, **Workflows**, **Screens**, **Fields**, **Permissions**, **Security**, and **Notifications**.
- **Practical Use**: Log Bugs and Tasks, track their progress through workflows, notify relevant team members.

| **Element** | **Mapping** | **Explanation** |
| --- | --- | --- |
| **Issue Type Scheme** | Project → Issue Type Scheme → Issue Types | Defines the types of issues (e.g., Bug, Task, Story) available in the project. |
| **Workflow Scheme** | Project → Workflow Scheme → Workflows | Controls the lifecycle (statuses and transitions) for each issue type. |
| **Screen Scheme** | Project → Issue Type Screen Scheme → Screen Schemes → Screens | Defines the fields displayed at different issue stages (Create, Edit, View screens). |
| **Field Configuration** | Project → Field Configuration Scheme → Field Configuration → Custom Fields | Controls the behavior (required, optional, hidden) of fields in the project. |
| [**Permission Scheme**](https://confluence.atlassian.com/adminjiraserver076/managing-project-permissions-945111102.html) | Project → Permission Scheme → Roles and Users/Group | Defines who can perform specific actions (e.g., create, edit, transition issues). |
| **Notification Scheme** | Project → Notification Scheme | Configures notifications for issue events (e.g., issue creation, status changes). |
| **Security Scheme** | Project → Issue Security Scheme → Security Levels → Roles/Users/Groups | Restricts visibility of specific issues to selected roles or users. |
| **Priorities Scheme** | Settings (⚙️)→ Priorities → Priority schemes | Defines the priority levels (e.g., Low, Medium, High, Critical) that can be assigned to issues. |
| **Project Roles** | Project → Project Roles → Users/Group | Assigns roles (e.g., Developer, Tester) to users or groups for project-specific permissions. |

---

## 📂 Create a Project

Follow the steps outlined in ****['Create a new project'](https://support.atlassian.com/jira-software-cloud/docs/create-a-new-project/) ****link to create a ['company managed project'](https://support.atlassian.com/jira-software-cloud/docs/what-are-team-managed-and-company-managed-projects/) named ‘**Bug Tracker’**.

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXcs3FRyl-cRXGgYp_LeXDA9dLmRHPmjynEWSWjNzE2DHuudBsb9ESgY_iy3XucY7EqxQIGoWGPNQ12w6yvipvOebgpOWJu9bFOJx5Jqf6aUTFB1Vn4QOGexzLcrP9hj7BDVxnV9QQ?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcs3FRyl-cRXGgYp_LeXDA9dLmRHPmjynEWSWjNzE2DHuudBsb9ESgY_iy3XucY7EqxQIGoWGPNQ12w6yvipvOebgpOWJu9bFOJx5Jqf6aUTFB1Vn4QOGexzLcrP9hj7BDVxnV9QQ?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXfPnh0pUBeK7q71r6fyMndU1Alid-sM7q4nIVvSBbj-tfYYLikYEYXu0z7dM2N6pJHH4fgO48yFz20H246yHub3ngfqeai9zO2X-Zb2z38GWsRV1cMX1BFugoOTEDgi1QGQYKz99A?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfPnh0pUBeK7q71r6fyMndU1Alid-sM7q4nIVvSBbj-tfYYLikYEYXu0z7dM2N6pJHH4fgO48yFz20H246yHub3ngfqeai9zO2X-Zb2z38GWsRV1cMX1BFugoOTEDgi1QGQYKz99A?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

---

## 🧑‍🤝‍🧑 Configure Project Roles.

### 🧑‍🤝‍🧑Add Project Roles

- Navigate to **Project Settings →People**. Assign roles to users or groups. Make sure these roles are already created, if not, follow the [article](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/).****
    - **Administrator**: Bella Gibson (Product Lead)
    - **Developer**: Harry Young
    - **QA**: Owen Black

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXd-vU-XcsZGFvvHPMlbe-OcCTO7qR7Ifq0FysIQculd75MNWs-mTZpEJKbdIoTk3hB1M6fqLfd3eda-OkBhbWbHAWQrL97zJTExg5VzTzt1HcxmcjYC1xqUwEYQvtQ4l-nbCnpbbA?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd-vU-XcsZGFvvHPMlbe-OcCTO7qR7Ifq0FysIQculd75MNWs-mTZpEJKbdIoTk3hB1M6fqLfd3eda-OkBhbWbHAWQrL97zJTExg5VzTzt1HcxmcjYC1xqUwEYQvtQ4l-nbCnpbbA?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

---

## 📋 Customizing Schemes for the Project

### 🧩 Issue Type Scheme

- **Custom Issue Type Scheme: ‘Bug Tracker Issue Type Scheme’**
- **Custom Issue Types:** Bug, Task, Improvement
- Associate the scheme with the **‘Bug Tracker”** project.

**Example Interaction:** QA and Developer log **Bugs & Tasks** issue for a software defect.

### 🧩Creating a Scheme

- Go to **Settings (⚙️)**  → **Issues → Issue Types → Issue type schemes.** Add a new issue type scheme named **‘Bug Tracker Issue Type Scheme’** by following the steps in the [article](https://support.atlassian.com/jira-cloud-administration/docs/add-edit-and-delete-an-issue-type-scheme/).
- **Add Bug and Task.**
- **Remove other issue types i (e.g., Epic, Story, Sub-task, if not required).**

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXcCr4pC7bf3hG_JVA_b41zk6BD9cdzr0QLZucvymbZI0e1aC_bR1XSTNjJ9Gu--yoIIVkK8dPPhtOiKzQanw-YzKyCUWM3IQ8nF9DNPb2Bb78fyCe4kL7EzsM310-KjY5B8xJBkzg?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcCr4pC7bf3hG_JVA_b41zk6BD9cdzr0QLZucvymbZI0e1aC_bR1XSTNjJ9Gu--yoIIVkK8dPPhtOiKzQanw-YzKyCUWM3IQ8nF9DNPb2Bb78fyCe4kL7EzsM310-KjY5B8xJBkzg?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🧩Associating Scheme with the Project

Now, go to the ‘**Bug Tracker’** project, then navigate to **Project Settings → Issue → Types**. Change the currently assigned Issue Type scheme to a **‘Bug Tracker Issue Type Scheme’**  scheme.

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXd32HF8EyTTBQKh22QcMOLL9Tg_j_0TFTer8_DmJGJhOBAYTrRWKBmWJcj4Ig_es9UwpIoi9Cv46lRTCxrq0ketvc2vJZkToIuqhJwn6ldgrcDGGtBkFyYU0mApKAcUhPacBYdt7A?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd32HF8EyTTBQKh22QcMOLL9Tg_j_0TFTer8_DmJGJhOBAYTrRWKBmWJcj4Ig_es9UwpIoi9Cv46lRTCxrq0ketvc2vJZkToIuqhJwn6ldgrcDGGtBkFyYU0mApKAcUhPacBYdt7A?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

**Note →** We will take care of Workflow, Field Configuration and Screen mapping to Issue Type Screen in the later steps.

### 🛠 Workflow Scheme

**Example Interaction:** An Issue moves through the defined workflow, transitioning from **‘Open → In Progress → In QA → Done.’**

### 🛠 Create a Workflow

- Go to **Settings (⚙️) → Issues → Workflows**, and create new workflows called **‘Bug and Task Workflow’** by following the steps outlined in the [article](https://support.atlassian.com/jira-work-management/docs/how-to-create-workflows/).
    - **For Bugs:** States: **Open → In Progress → In QA → Done.**

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXc0zSanBheTyuMwE34wVQZ0BaP9vviEt00xH7lX8zLJLoqR-I-RyYc7Jhr8pOoFfPXloXUcBiUTBgGhbptizVn0iqUjVqCE75R54JDnbm7A-QhOJtPPI_Y31BX8UQ2SPilFPFL2vA?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc0zSanBheTyuMwE34wVQZ0BaP9vviEt00xH7lX8zLJLoqR-I-RyYc7Jhr8pOoFfPXloXUcBiUTBgGhbptizVn0iqUjVqCE75R54JDnbm7A-QhOJtPPI_Y31BX8UQ2SPilFPFL2vA?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

- **Transitions:** For **‘Bug and Task Workflow’**. Restrict the transition to **‘Done’** only for QA roles. To know more about transition, read the [article](https://support.atlassian.com/jira-cloud-administration/docs/work-with-issue-workflows/).

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXdxaKhtvESMXMLs2LVlXX5YEGrGKMVnwtze6orpwguiw2B9kKwPM_xkYBE7FQC2x8uniCHjGEH0_1YHIoRU3s_04Kr25B6hTmRAnNAPgrwoXltJr_pUfwcxYTgMV4NwLMUAJWz_Dg?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdxaKhtvESMXMLs2LVlXX5YEGrGKMVnwtze6orpwguiw2B9kKwPM_xkYBE7FQC2x8uniCHjGEH0_1YHIoRU3s_04Kr25B6hTmRAnNAPgrwoXltJr_pUfwcxYTgMV4NwLMUAJWz_Dg?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🛠 Create a Workflow Scheme

- Next, create a new workflow scheme named **‘Bug Tracker Workflow Scheme’** and add **‘Bug and Tasks Workflow’** for the **‘Bug’** and **‘Task’** issue types.

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXeZMrLAgZ34ahOSzcJsDLNaVp4yk_c_vN-nlBntQIue0o0jkeCmqbbfAJu7tp6t5DRaH7IAatUfrgSiIyI9hL0siKXIMFkOtW9KRwcbC6WgPqE2FSoAyILPUNCgiYWiQ9MML1A0QQ?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeZMrLAgZ34ahOSzcJsDLNaVp4yk_c_vN-nlBntQIue0o0jkeCmqbbfAJu7tp6t5DRaH7IAatUfrgSiIyI9hL0siKXIMFkOtW9KRwcbC6WgPqE2FSoAyILPUNCgiYWiQ9MML1A0QQ?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🛠 Associate the Workflow Scheme to Project

- **Now, go to the ‘Bug Tracker’ project, then navigate to Project Settings → Workflows. Switch the currently assigned Workflow scheme to the ‘Bug Tracker Workflow Scheme’ .**

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXc-aw86CjA8aXINdsv1UR7EUkAtwLEXWfFumoL1JMVgMUYZRIWJYR9-RJ6wSl5cWbqXtJHbERVkfgCFLTHkIy6FsdPQrpbWXXNKOGBpOTVe7w5OaL7HDuhwR03Ogw7Ztc8UE1gyyQ?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc-aw86CjA8aXINdsv1UR7EUkAtwLEXWfFumoL1JMVgMUYZRIWJYR9-RJ6wSl5cWbqXtJHbERVkfgCFLTHkIy6FsdPQrpbWXXNKOGBpOTVe7w5OaL7HDuhwR03Ogw7Ztc8UE1gyyQ?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 📋 Screen Scheme

**Example Interaction:** The Bug Create Screen shows **Summary**, **Description**, and **Priority,** while the Edit Screen allows adding **Assignee.**

### 📋Create Screens

- Go to **Settings (⚙️) → Issues → Screens → Screens**, and create new screens A screen is an arrangement of fields that are displayed when the issue is created, edited or transitioned through workflow. Define screens as the following. :
- **Create_Screen**: Fields like Summary, Description, Priority.
- **Edit_Screen**: Add fields like Assignee and Labels.
- **View_Screen**: Show all fields.

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXfxIv_CBE5KKdQhd7Ok9qrCi1IZyWtwY4nk4uC2ob0WbROLKKGjts0P1lSexEn2M3OaGzElS7eQwuZ7wXlqpHXiiS5wIXlHGbULTvYpfFkNmSATNh7pHUlTHKHC9_0_wIXuDMgCVA?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfxIv_CBE5KKdQhd7Ok9qrCi1IZyWtwY4nk4uC2ob0WbROLKKGjts0P1lSexEn2M3OaGzElS7eQwuZ7wXlqpHXiiS5wIXlHGbULTvYpfFkNmSATNh7pHUlTHKHC9_0_wIXuDMgCVA?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 📋Create a Screen Scheme

- Create a new Screen Schemes called **‘Bug Tracker Screen Scheme’** by following the steps outlined in the [article](https://support.atlassian.com/jira-cloud-administration/docs/configure-issue-screens/) and create an Issue Operation mapping with previously created screen. This configuration decided which screen will be displayed for each issue operation.

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXe0x_6Js_oHIwuX0Y9LG8XvY8fxpoZ0oI1mRbLN5g5URs88vk13xzSobkbGEdo9k9AUciCUn3Cpv0UZNyanUB7qBbUfXwj8tuNUrU2SNaUylaJRdht33OTgg1DoNX_8S9RIUGDFKA?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe0x_6Js_oHIwuX0Y9LG8XvY8fxpoZ0oI1mRbLN5g5URs88vk13xzSobkbGEdo9k9AUciCUn3Cpv0UZNyanUB7qBbUfXwj8tuNUrU2SNaUylaJRdht33OTgg1DoNX_8S9RIUGDFKA?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 📋Create an Issue Type Screen Scheme

- **Associate Screens with Issue Operation:** Create a **‘Bug Tracker Issue Type Screen Scheme’** and ****map the appropriate **Screen Scheme** to the **Issue Type** (i.e., **‘Bug’** and **‘Task’ )**. The Issue Type Screen Scheme is associated to a project to define the issue layout.

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXdDGiRu3YXT0rQKRbljX7GBNwUf197N00l2nIo9x9izilKalWu39mWUyt4KHXdJ0ZctXyfESEwjSZa4FTo1TqIb8l4zcm0VFHj89MXah6bOMcYR3cAqLPVYq43I8ViBvLVFVCr3Lw?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdDGiRu3YXT0rQKRbljX7GBNwUf197N00l2nIo9x9izilKalWu39mWUyt4KHXdJ0ZctXyfESEwjSZa4FTo1TqIb8l4zcm0VFHj89MXah6bOMcYR3cAqLPVYq43I8ViBvLVFVCr3Lw?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 📋Associate Screens to the Project

- **Now, go to the “Bug Tracker” project, then navigate to Project Settings → Screen. Change the currently assigned Issue Type Screen Schemes to a previously created  ‘Bug Tracker Issue Type Screen Scheme’  .**

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXcEP3-SuUtqKcfeM6_wBCXQnWFTvJi3sq_5RYAHA4BQkE5-Di7WFAu9zYtfkUHAC5MjQx6G9DnELdsZxLqHPh5Gm5mQwY4HByTihfrM390umdj5uNctjDggd2JkxA91WtcVVh-hKA?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcEP3-SuUtqKcfeM6_wBCXQnWFTvJi3sq_5RYAHA4BQkE5-Di7WFAu9zYtfkUHAC5MjQx6G9DnELdsZxLqHPh5Gm5mQwY4HByTihfrM390umdj5uNctjDggd2JkxA91WtcVVh-hKA?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🖋 Field Configuration

**Example Interaction**: While creating a Bug or Task, the **Bug Priority** field must be filled.

### 🖋 Create a new Custom Field

- Go to **Settings (⚙️) → Issues → Fields→Custom fields**, and create new custom fields called **"Bug Priority"** by following the steps outlined in the [article](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/). This will be visible in **‘Create_Screen’** and **‘View_Screen’** Screens created earlier.

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXcv5tzAPCrHQxG9XsbJaFdr4Ikn78T4FdAQctojHXgtvymqincS3YevpcqcW7npZ9N42PahB_64OOYjSfuM5HIjtMYSYv5Jt6d8X8_Gg4oIfN2GSDW_Ys3axjzKqUxqhLKP6ZWI?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcv5tzAPCrHQxG9XsbJaFdr4Ikn78T4FdAQctojHXgtvymqincS3YevpcqcW7npZ9N42PahB_64OOYjSfuM5HIjtMYSYv5Jt6d8X8_Gg4oIfN2GSDW_Ys3axjzKqUxqhLKP6ZWI?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🖋 Create a new Field Configuration

- Create a new Field Configuration **‘Bug Tracker Field configuration’** *(easier approach is by copying the default one)* and make sure the custom fields are the following. ;
    - **Bug Priority** is mandatory for all Bugs and Tasks.

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXc3IT5FyYyuGIWJ3NelrAkcjf7ZLaKDDnVWVR62qSMnBgPTBay4N3FDmhhpqJIIGJFf-NEHj6KfH3MNjtKYZikBW01lb8ImiBBkMYtKo8yHjrAG1EKpsdQVSdMhXJTK9rSUwrwKhQ?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc3IT5FyYyuGIWJ3NelrAkcjf7ZLaKDDnVWVR62qSMnBgPTBay4N3FDmhhpqJIIGJFf-NEHj6KfH3MNjtKYZikBW01lb8ImiBBkMYtKo8yHjrAG1EKpsdQVSdMhXJTK9rSUwrwKhQ?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXf_v5GKACwIUq4STY6-jaBZCD6-MxmjWE-e8buWp7nTr4wzNGI9rsHTX0hQqOP4TDgdHNhCv4l6vda_0ipKAj33z03CVVwD5XRNSmaju9e1zoLD8KIF5D6KPQf4s2axibTb9lau?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf_v5GKACwIUq4STY6-jaBZCD6-MxmjWE-e8buWp7nTr4wzNGI9rsHTX0hQqOP4TDgdHNhCv4l6vda_0ipKAj33z03CVVwD5XRNSmaju9e1zoLD8KIF5D6KPQf4s2axibTb9lau?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🖋 Create a new Field Configuration Scheme

- Create a new Field Configuration Scheme **‘Bug Tracker Field Configuration Scheme’** and associate the **“Bug Tracker Field configuration”** Field configuration to the issue type **Bug and Task**.

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXfat5Oi4RPKP4HRPVJEeYaiLJCSw9BbnKVSETPjV3_2HFsqyGZm51IgwzjaTWHtmlCf_yXY07BQM1VUjQNyjSN9c5PylThXmdyU1yIk6nJwj4r-QAPjo77pjp5IU33SnO7gTXsO5Q?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfat5Oi4RPKP4HRPVJEeYaiLJCSw9BbnKVSETPjV3_2HFsqyGZm51IgwzjaTWHtmlCf_yXY07BQM1VUjQNyjSN9c5PylThXmdyU1yIk6nJwj4r-QAPjo77pjp5IU33SnO7gTXsO5Q?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🖋 Associate the Field Configuration Scheme to a Project

- **Now, go to the ‘Bug Tracker’ project, then navigate to Project Settings → Issues→ Fields change the currently assigned Field configuration scheme to a previously created ‘Bug Tracker Field Configuration Scheme’ . This makes Bug Priority custom field mandatory for issue type bugs.**

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXdKCyfjR0SJQ7rcqmY6d4e1f6vJOXaI9FiWyTkGmIxhyUp16pfkSXKwF8iDYg3a0O1ejSDu6R5Wwsx1NJFv0VOr4I1limke31ye0oi0g50Xns0Qg3Zy6ATFHRyO_YUpQ70WhGbC?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdKCyfjR0SJQ7rcqmY6d4e1f6vJOXaI9FiWyTkGmIxhyUp16pfkSXKwF8iDYg3a0O1ejSDu6R5Wwsx1NJFv0VOr4I1limke31ye0oi0g50Xns0Qg3Zy6ATFHRyO_YUpQ70WhGbC?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 📜 Permission Scheme

**Example Interaction:** Only Project **Administrator**, **Developer** and **QA** Roles can transition as issue.

- Project Lead: Full Access
- Developer: Full Issue and Comments Permissions
- QA: Full Issue and Comments Permissions

### 📜Create a new Permission Scheme

- Go to **Settings (⚙️) → Issues → Permission Scheme**,
- Create a new Permission Scheme **‘Bug Tracker Permission Scheme’** (easier approach is by copying the default one) and make sure that only **Developer** and **QA Roles** can transition as issue.

### 📜Assign Permissions

The previous created **QA** and **Developer** Role have been granted **Issue and Comments** Permissions. **Administrator** Role has all permissions. Refer to the article [‘Managing Project Permissions’](https://confluence.atlassian.com/adminjiraserver076/managing-project-permissions-945111102.html) for more information.

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXcX8JcF80e07ef4mtCWobPYm3C2a7cR2IiUx97WBq-HXSFaKPjtYlKHGbTDI4n6CD4e7VR_ajmx1WIEoagF22lPLWe_81I0T3XYNJZW0Qv03HzYW7rB5m1qlDLiHX_0JoWn-x4Hcg?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcX8JcF80e07ef4mtCWobPYm3C2a7cR2IiUx97WBq-HXSFaKPjtYlKHGbTDI4n6CD4e7VR_ajmx1WIEoagF22lPLWe_81I0T3XYNJZW0Qv03HzYW7rB5m1qlDLiHX_0JoWn-x4Hcg?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 📜Associate Permission Scheme to the Project

- Associate a **‘bug tracker permission scheme’** to the **‘Bug Tracker’** project by navigating to **Project Settings → Permissions**.

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXcJ_Chtv0qUwTsLZ18Q_JM8Ah0P1p57CGZqajhA-zrNfmzFeJ0E_yvEV4Z7NietVCZMenrPgxZVtmgzaEsxEHAL0uKMu5TLJwIayFk_0gt-F1mQ84vcFYM2JrlDo1lyOoAF1J6yRw?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcJ_Chtv0qUwTsLZ18Q_JM8Ah0P1p57CGZqajhA-zrNfmzFeJ0E_yvEV4Z7NietVCZMenrPgxZVtmgzaEsxEHAL0uKMu5TLJwIayFk_0gt-F1mQ84vcFYM2JrlDo1lyOoAF1J6yRw?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🔔 Notification Scheme

**Example Interaction:** A notification is sent to the **Project Lead, Reporter, Project Role (Administrators)** and **All Watchers** when a new issue is created. Notify **Assignee** on issue assignment.

### 🔔Create a new notification Scheme

- Go to **Settings (⚙️) → Issues → Notification Scheme**,
- Create a new Notification Scheme **‘Bug Tracker Notification Scheme’** (easier approach is by copying the default one) and update the Notification Scheme:

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXfzZ_4TMAuguCEaWHCYVQ6oiAoB2pM0tCl-HSZFm6TqGk-8SCHC3FHNc8Ee9IWhVO6cenaweVQF7rj5BhtI2253FZlRUx9g89QeRA0gx_VZytnzSYTgIY9n987p6hGk6cDzc0St?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfzZ_4TMAuguCEaWHCYVQ6oiAoB2pM0tCl-HSZFm6TqGk-8SCHC3FHNc8Ee9IWhVO6cenaweVQF7rj5BhtI2253FZlRUx9g89QeRA0gx_VZytnzSYTgIY9n987p6hGk6cDzc0St?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🔔Add Notification Rules in the Scheme

Add the following notification rules in the **‘Bug Tracker Notification Scheme’**

- Notify **Project Lead, Reporter, Project Role (Administrators)**  and **All Watchers** when an issue is created.
- Notify the **Assignee** when an issue is transitioned.

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXfcaioa8lahmiIHDnBY-kCyKBYvNxVL2y0x6O9FUPqkIcIPgpvVnqeL_SzmuigMPyiyXccExKvMTThmLUyjvmhpdNQZTOUo1nQca6QSKNN57WYewU1CxWtuhO3Mkl9RO-9rmFU8ow?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfcaioa8lahmiIHDnBY-kCyKBYvNxVL2y0x6O9FUPqkIcIPgpvVnqeL_SzmuigMPyiyXccExKvMTThmLUyjvmhpdNQZTOUo1nQca6QSKNN57WYewU1CxWtuhO3Mkl9RO-9rmFU8ow?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🔔Associate Notification Screen Scheme to the Project

- **Now, go to the ‘Bug Tracker’ project, then navigate to Project Settings → Notification→ Settings, change the currently assigned notification scheme to a previously created ‘Bug Tracker Notification Scheme’ .**

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXdXQXQ8n_oCVNyasrKn7jP25py-4rPPP3A5KNF0RE4JqD28e-CwbTsbP1BIMnZ8a8N3oKv4vIm00qFTgZlDYime5Y9esFYcw7uCEUgTa_XkImNrvJsKScUSCkLq3OMVAGizYNWSFA?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdXQXQ8n_oCVNyasrKn7jP25py-4rPPP3A5KNF0RE4JqD28e-CwbTsbP1BIMnZ8a8N3oKv4vIm00qFTgZlDYime5Y9esFYcw7uCEUgTa_XkImNrvJsKScUSCkLq3OMVAGizYNWSFA?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🔒 Security Scheme

**Example Interaction:** Security vulnerabilities, need to be restricted to Administrator Role.

### 🔒 Create a new Security Scheme

1. Go to **Settings (⚙️) → Issues → Issue Security Scheme**,
2. Create a new Notification Scheme **‘Bug Tracker Issue Security Scheme’** (easier approach is by copying the default one)

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXdMXj0zgYguqqEA0r_6CMVnLnhDizKpOMrI41zo-UHwnv7p7qZ6UP_UqsJFi3v1FK3ScHhlPzFD4-rMzN94hq_tqBj5lnqoKi9yoKaycZg_kiQfKgIGQiGzb7jyDXC7aDPJfKZE?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdMXj0zgYguqqEA0r_6CMVnLnhDizKpOMrI41zo-UHwnv7p7qZ6UP_UqsJFi3v1FK3ScHhlPzFD4-rMzN94hq_tqBj5lnqoKi9yoKaycZg_kiQfKgIGQiGzb7jyDXC7aDPJfKZE?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🔒Update the Security Scheme

Add **Security Levels**:

- **No Restriction (Default)**: Visible to all project members. **This should be the default one.**
- **Restricted**: Visible only Administrators roles .

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXc5QKukCZNrAIvJRp493d29Tf0l1t8lDXSkF5URC1JzLDdd1fxiaxMM1FIrSewhZkibiIWnrAlQANdCxMG89giFd91LK6At364CZGltWlxAYNLu7vSl97qdQBIMx6QPW51u9mcutA?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc5QKukCZNrAIvJRp493d29Tf0l1t8lDXSkF5URC1JzLDdd1fxiaxMM1FIrSewhZkibiIWnrAlQANdCxMG89giFd91LK6At364CZGltWlxAYNLu7vSl97qdQBIMx6QPW51u9mcutA?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🔒Associate the Security Scheme to Project

- **Now, go to the ‘Bug Tracker’ project, then navigate to Project Settings →Security→, change the currently assigned security scheme to a previously created ‘Bug Tracker Issue Security Scheme’ .**

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXdI7TplJLlh6jOoc1zNFrlhhftNs3uL7Lti47HPjN9RoTnGWIul6qVgFl7hsHsPd1RZRGlvE8kkmBY6romS8ThijpPl3HQYLuZ9ZVT9Nfwn-ZjxjXFZlZ5RqJ45zxJTI9lhYRYe?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdI7TplJLlh6jOoc1zNFrlhhftNs3uL7Lti47HPjN9RoTnGWIul6qVgFl7hsHsPd1RZRGlvE8kkmBY6romS8ThijpPl3HQYLuZ9ZVT9Nfwn-ZjxjXFZlZ5RqJ45zxJTI9lhYRYe?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🎨 Priorities Scheme

**Example Interaction:** The Project has only 3 Priorities.; **High, Medium, Low (Pre-existing)**

### 🎨 Create a new Priority Scheme

- Create a new Priority Scheme **‘Bug Tracker Priority Scheme’** by following the ['Manage priority scheme's](https://support.atlassian.com/jira-cloud-administration/docs/manage-priority-schemes/) article.
- Associate the available Priorities to the **‘Bug Tracker Priority Scheme’**.****

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXf0X1vg8nwJC-ZM8hchmpP7ldNK-tRVevkvFHJu2zPFGXJOqriGJ-R3F_gH8dE_HFRbNiuXbOvL_wke5jUA02VXcHJYvoGCM4uOhKaLiBT84-uZwW4QwyQRWZC7EIWPyNSufwd1jA?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf0X1vg8nwJC-ZM8hchmpP7ldNK-tRVevkvFHJu2zPFGXJOqriGJ-R3F_gH8dE_HFRbNiuXbOvL_wke5jUA02VXcHJYvoGCM4uOhKaLiBT84-uZwW4QwyQRWZC7EIWPyNSufwd1jA?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

### 🎨 Associate the Priority Scheme to the Project

Add the **‘Bug Tracker Priority Scheme’** to **‘Bug Tracker’** Project from the Priority schemes pages.****

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXfC_FDJgxtTy5ydtuhwegimygGGms7dFySo_FS4INQtsp0zjIJ_kZ8pQBWaYlIUv7V-rosXQHoSHd_SBT06CZy7acROBlYK-G8v-AcCVWAm9pGXo46s4SOpZbANa0k1FrGxE-6R?key=UD7TJ8OdiB7fOqKjKG7w8zmo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfC_FDJgxtTy5ydtuhwegimygGGms7dFySo_FS4INQtsp0zjIJ_kZ8pQBWaYlIUv7V-rosXQHoSHd_SBT06CZy7acROBlYK-G8v-AcCVWAm9pGXo46s4SOpZbANa0k1FrGxE-6R?key=UD7TJ8OdiB7fOqKjKG7w8zmo)

---