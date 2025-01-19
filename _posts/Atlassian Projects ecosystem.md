
<p></p>
<p><a href="#h.8m8u7sa3l79y">Support Project Types        1</a></p>
<p><a href="#h.a1pvozpl6b2o">Workflow Representation of JIRA Elements        2</a></p>
<p><a href="#h.n5glj9l2s0xz">Comprehensive Guide to JIRA Project Creation and Modification (Example-Based Learning)        2</a></p>
<p><a href="#h.ilz4tgppy5sd">📂 Create a Project        3</a></p>
<p><a href="#h.3il65pey3wov">🧑‍🤝‍🧑 Configure Project Roles.        4</a></p>
<p><a href="#h.6tnky0t297xy">📋 Customizing Schemes for the Project        4</a></p>
<p><a href="#h.mjdnf5re2vvg">🧩 Issue Type Scheme        4</a></p>
<p><a href="#h.e0vqyi3zsr4f">🛠 Workflow Scheme        5</a></p>
<p><a href="#h.hx3gct3bzbvv">📋 Screen Scheme        6</a></p>
<p><a href="#h.7liljmb8rteo">🖋 Field Configuration        9</a></p>
<p><a href="#h.3p08ju3enfrs">📜 Permission Scheme        10</a></p>
<p><a href="#h.1zq4eh6ij46x">🔔 Notification Scheme        11</a></p>
<p><a href="#h.nsdq4epw5mz5">🔒 Security Scheme        12</a></p>
<p><a href="#h.lfgvbpecl4he">🎨 Priorities Scheme        14</a></p>
<hr>
<h2>Support Project Types </h2>
<table>
<tbody>
<tr>
<td colspan="1" rowspan="1">
<p>Product Name</p></td>
<td colspan="1" rowspan="1">
<p>Project Type</p></td>
<td colspan="1" rowspan="1">
<p>Unique Issue Types</p></td>
<td colspan="1" rowspan="1">
<p>Standard Issue Types</p></td>
<td colspan="1" rowspan="1">
<p>Management Type</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Jira Product Discovery</p></td>
<td colspan="1" rowspan="1">
<p>Product Discovery</p></td>
<td colspan="1" rowspan="1">
<p>Ideas</p></td>
<td colspan="1" rowspan="1">
<p>Task, Sub-task</p></td>
<td colspan="1" rowspan="1">
<p>Team-managed only</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Jira Service Management</p></td>
<td colspan="1" rowspan="1">
<p>Service Management</p></td>
<td colspan="1" rowspan="1">
<p>Request, Incident, Problem, Change, Service Request</p></td>
<td colspan="1" rowspan="1">
<p>Task, Sub-task, Custom Request Types</p></td>
<td colspan="1" rowspan="1">
<p>Company and Team-managed</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Jira</p></td>
<td colspan="1" rowspan="1">
<p>Software Projects</p></td>
<td colspan="1" rowspan="1">
<p>Epic, Story, Bug</p></td>
<td colspan="1" rowspan="1">
<p>Task, Sub-task</p></td>
<td colspan="1" rowspan="1">
<p>Company and Team-managed</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Jira Work Management</p></td>
<td colspan="1" rowspan="1">
<p>Business Projects</p></td>
<td colspan="1" rowspan="1">
<p>None</p></td>
<td colspan="1" rowspan="1">
<p>Task, Sub-task</p></td>
<td colspan="1" rowspan="1">
<p>Company and Team-managed</p></td></tr></tbody></table>
<hr>
<p></p>
<h2>Workflow Representation of JIRA Elements </h2>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXczhgpaAnmzPu45LWoylNzImFb67JifqGvSarkUM38lXNDWzAKWfKoDGtLIPh_Ex06SK75h0kuZIuiC4EsijWuXc6uU6hc3zAhKxYAkzmZxrpMHqcW4lRaSxiPbtneWwPM?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h2>Comprehensive Guide to JIRA Project Creation and Modification (Example-Based Learning)</h2>
<p>Let’s set up a company managed Jira project for a software development team. The goal is to manage (Bugs and Tasks) Issue Types , ensuring that issues move through their respective workflows, fields are configured correctly, and notifications reach the right people.</p>
<ul>
<li>Setup Objective: Configure schemes for Issue Types, Workflows, Screens, Fields, Permissions, Security, and Notifications.</li>
<li>Practical Use: Log Bugs and Tasks, track their progress through workflows, notify relevant team members.  </li></ul>
<table>
<tbody>
<tr>
<td colspan="1" rowspan="1">
<p>Element</p></td>
<td colspan="1" rowspan="1">
<p>Mapping</p></td>
<td colspan="1" rowspan="1">
<p>Explanation</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Issue Type Scheme</p></td>
<td colspan="1" rowspan="1">
<p>Project → Issue Type Scheme → Issue Types</p></td>
<td colspan="1" rowspan="1">
<p>Defines the types of issues (e.g., Bug, Task, Story) available in the project.</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Workflow Scheme</p></td>
<td colspan="1" rowspan="1">
<p>Project → Workflow Scheme → Workflows</p></td>
<td colspan="1" rowspan="1">
<p>Controls the lifecycle (statuses and transitions) for each issue type.</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Screen Scheme</p></td>
<td colspan="1" rowspan="1">
<p>Project → Issue Type Screen Scheme → Screen Schemes → Screens</p></td>
<td colspan="1" rowspan="1">
<p>Defines the fields displayed at different issue stages (Create, Edit, View screens).</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Field Configuration</p></td>
<td colspan="1" rowspan="1">
<p>Project → Field Configuration Scheme → Field Configuration → Custom Fields</p></td>
<td colspan="1" rowspan="1">
<p>Controls the behavior (required, optional, hidden) of fields in the project.</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p><a href="https://confluence.atlassian.com/adminjiraserver076/managing-project-permissions-945111102.html">Permission Scheme</a></p></td>
<td colspan="1" rowspan="1">
<p>Project → Permission Scheme → Roles and Users/Group</p></td>
<td colspan="1" rowspan="1">
<p>Defines who can perform specific actions (e.g., create, edit, transition issues).</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Notification Scheme</p></td>
<td colspan="1" rowspan="1">
<p>Project → Notification Scheme</p></td>
<td colspan="1" rowspan="1">
<p>Configures notifications for issue events (e.g., issue creation, status changes).</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Security Scheme</p></td>
<td colspan="1" rowspan="1">
<p>Project → Issue Security Scheme → Security Levels → Roles/Users/Groups</p></td>
<td colspan="1" rowspan="1">
<p>Restricts visibility of specific issues to selected roles or users.</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Priorities Scheme</p></td>
<td colspan="1" rowspan="1">
<p>Settings (⚙️)→ Priorities → Priority schemes</p></td>
<td colspan="1" rowspan="1">
<p>Defines the priority levels (e.g., Low, Medium, High, Critical) that can be assigned to issues.</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Project Roles</p></td>
<td colspan="1" rowspan="1">
<p>Project → Project Roles → Users/Group</p></td>
<td colspan="1" rowspan="1">
<p>Assigns roles (e.g., Developer, Tester) to users or groups for project-specific permissions.</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Issue Features</p></td>
<td colspan="1" rowspan="1">
<p>Project → Issue Features</p></td>
<td colspan="1" rowspan="1">
<p>Adds specific functionalities to issues like linking, time tracking.</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Issue Attributes</p></td>
<td colspan="1" rowspan="1">
<p>Project → Issue Attributes</p></td>
<td colspan="1" rowspan="1">
<p>Defines the characteristics of issues like Statutes and Resolution.</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Project Components</p></td>
<td colspan="1" rowspan="1">
<p>Project → Components</p></td>
<td colspan="1" rowspan="1">
<p>Breaks down the project into logical modules or areas (e.g., Frontend, Backend).</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Project Versions</p></td>
<td colspan="1" rowspan="1">
<p>Project → Versions</p></td>
<td colspan="1" rowspan="1">
<p>Tracks versioned releases or milestones (e.g., v1.0, v2.0) for the project.</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Project Category</p></td>
<td colspan="1" rowspan="1">
<p>Project → Category</p></td>
<td colspan="1" rowspan="1">
<p>Groups related projects under a category (e.g., Internal Projects, Client Projects.</p></td></tr>
<tr>
<td colspan="1" rowspan="1">
<p>Automation Rules</p></td>
<td colspan="1" rowspan="1">
<p>Project → Automation Rules</p></td>
<td colspan="1" rowspan="1">
<p>Automates repetitive tasks (e.g., auto-assigning issues, sending reminders for due dates.</p></td></tr></tbody></table>
<hr>
<p></p>
<h2>📂 Create a Project</h2>
<p>Follow the steps outlined in <a href="https://support.atlassian.com/jira-software-cloud/docs/create-a-new-project/">“Create a new project”</a> link to create a <a href="https://support.atlassian.com/jira-software-cloud/docs/what-are-team-managed-and-company-managed-projects/">company managed project </a>named ‘Bug Tracker’.</p>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXebTHWX5EIDf2WecSpHZCakrab13Kv5k6-jmlebFVlXha0MaqmUuFKLr_b0AAHxbLTNxco4SlygoywO_oIYa1qVZbzWNmIuPOOSeDpLWy0u6Wz92M8ZxcVhygT5UBCSAgM?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXc110N2FuiLVT_chb3JH9wMdiC2v16lkuOl5QKekPaEioN0pKtCZlPTHtZFaGDJqw2Yu7ps7PA5pGzfg87nOcJLlc6gqBbRkZp9YmUIqyBPXmxp0aV0glvYiE35Y2U2uac?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<hr>
<p></p>
<h2>🧑‍🤝‍🧑 Configure Project Roles. </h2>
<h4>🧑‍🤝‍🧑Add Project Roles </h4>
<ul>
<li>Navigate to Project Settings →People. Assign roles to users or groups. Make sure these roles are already created, if not, follow the <a href="https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/">article</a>. </li></ul>
<ul>
<li>Administrator: Bella Gibson (Product Lead)</li>
<li>Developer: Harry Young</li>
<li>QA: Owen Black</li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdFSsXXFD1wG0evxbAaTGNYFNh86zpmP8jNCN_ELi_sC7FARTcryZSZDbwik5vHQMPraUpAXalkmUMrZdCxmgUD4XhxUP5O_W9K0QeFUOYhbhxNUdf2dYzhoIa-WqKaqHA?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<hr>
<p></p>
<h2>📋 Customizing Schemes for the Project</h2>
<h3>🧩 Issue Type Scheme</h3>
<ul>
<li>Custom Issue Type Scheme: ‘Bug Tracker Issue Type Scheme’</li>
<li>Custom Issue Types: Bug, Task, Improvement</li>
<li>Associate the scheme with the ‘Bug Tracker” project. </li></ul>
<p>Example Interaction: QA and Developer log Bugs & Tasks issue for a software defect.</p>
<h4>🧩Creating a Scheme</h4>
<ul>
<li>Go to Settings (⚙️)  → Issues → Issue Types → Issue type schemes. Add a new issue type scheme named ‘Bug Tracker Issue Type Scheme’ by following the steps in the <a href="https://support.atlassian.com/jira-cloud-administration/docs/add-edit-and-delete-an-issue-type-scheme/">article</a>. </li>
<li>Add Bug and Task.</li>
<li>Remove other issue types i (e.g., Epic, Story, Sub-task, if not required).</li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcg1WLPEIz4wUME8VbXkzTbkuGbTPeNE6x88KSzU9QcOmZs6nh5glTtM92ms-Ozya55CqmBqIiT-3BQWMX9svop1mhrorLYOZ7hVHvTWmZmekgPUsw1j4rIhRbRGMnfNuE?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>🧩Associating Scheme with the Project </h4>
<p>Now, go to the ‘Bug Tracker’ project, then navigate to Project Settings → Issue → Types. Change the currently assigned Issue Type scheme to a ‘Bug Tracker Issue Type Scheme’  scheme.</p>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdm_hBwaSFyC3Z6HLKK7L2iG_dwsir2N9MUzJefX1gqrz6_v1PBqMocd8yUXd9Za9jTKJC2lHCQLfLVzl_sLqP29pVDxvC98eoRQMKGrDCMcO4ZGeQZsPFIs3cKaOFkKoI?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<p>Note → We will take care of Workflow, Field Configuration and Screen mapping to Issue Type Screen in the later steps. </p>
<h3>🛠 Workflow Scheme</h3>
<p>Example Interaction: An Issue moves through the defined workflow, transitioning from ‘Open → In Progress → In QA → Done.’</p>
<h4>🛠 Create a Workflow</h4>
<ul>
<li>Go to Settings (⚙️) → Issues → Workflows, and create new workflows called ‘Bug and Task Workflow’ by following the steps outlined in the <a href="https://support.atlassian.com/jira-work-management/docs/how-to-create-workflows/">article</a>.</li></ul>
<ul>
<li>For Bugs: States: Open → In Progress → In QA → Done.</li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfwVO7VsoOdvltuGBsoGaQ68DmZTgrFlnohabtTZx14MTEpOu9X2D4rXPMuU4KLP-Ck_5lLP8KIvhTUkO4JB3pLH2_IldbCDloaECM3jSqQ4_XWTN7zrXbtzcYP4Mbf1Ww?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<ul>
<li>Transitions: For  ‘Bug and Task Workflow’. Restrict the transition to ‘Done’ only for QA roles. To know more about transition, read the <a href="https://support.atlassian.com/jira-cloud-administration/docs/work-with-issue-workflows/">article</a>. </li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfp_uIR3XFRS4b75p5CuyuVqSdHQobt59K_QPn_fsxaWlhNl6jmFHR0T12jB8_XCRBLRJvYdbrMvA4gxN-HWGMH5BWbQZzjaO5UZDDuP9JCNM54MEL75KRTYvrFK6_j_Sg?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>🛠 Create a Workflow Scheme</h4>
<ul>
<li>Next, create a new workflow scheme named ‘Bug Tracker Workflow Scheme’ and add ‘Bug and Tasks Workflow’ for the ‘Bug’ and ‘Task’ issue types.</li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeRffyoQgc59ncOnCC3xVCJmwLv4j6zP5RDOsWO_kwvsIlbL40-U2lrxu5c_nRSMZ-x_mnBccAp9VNLF_GtKsb84Eb1aLjHlFTX2G9y3E-yLamJUVetfkcJmqtQV3E7ct8?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>🛠 Associate the Workflow Scheme to Project</h4>
<ul>
<li>Now, go to the ‘Bug Tracker’ project, then navigate to Project Settings → Workflows. Switch the currently assigned Workflow scheme to the ‘Bug Tracker Workflow Scheme’ .</li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcmn6NWHlHK4BX-n2qhGkyzJwvBiFLdepObPouazYsajZEQd0KQNr1Oh3R4PcklUUtyEzcLlcGdujJgXiqnzwBCzaSC9Fn1zaPa-plJjV8dNdFo-enho4dtCvfrU5SRQUc?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h3>📋 Screen Scheme</h3>
<p>Example Interaction: The Bug Create Screen shows Summary, Description, and Priority, while the Edit Screen allows adding Assignee.</p>
<h4>📋Create Screens</h4>
<ul>
<li>Go to Settings (⚙️) → Issues → Screens → Screens, and create new screens A screen is an arrangement of fields that are displayed when the issue is created, edited or transitioned through workflow. Define screens as the following. :</li></ul>
<ul>
<li>Create_Screen: Fields like Summary, Description, Priority.</li>
<li>Edit_Screen: Add fields like Assignee and Labels.</li>
<li>View_Screen: Show all fields.</li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfsVTTpBpDAJ0pZHj1rlL7O5cCv1GGSS7GYTZoojLsPz5kM32gk39HLrS1V2F2abu2_7gsHh8wr42zDsOftOgnHlMD96AGp2UuLf0K0NlzSMrdMiIvmoPWPs2LC8Ur8kug?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>📋Create a Screen Scheme</h4>
<ul>
<li>Create a new Screen Schemes called ‘Bug Tracker Screen Scheme’ by following the steps outlined in the <a href="https://support.atlassian.com/jira-cloud-administration/docs/configure-issue-screens/">article</a> and create an Issue Operation mapping with previously created screen. This configuration decided which screen will be displayed for each issue operation.</li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe2affjKlNbmEG6zygb4mNnF8wFKcjTxkZefWt6-rnP84acRUyIL41hdFnXfT-v74nj_UqikMt9xKZIvSwLdv1MjQnyYX7xfuUw5OG-f4iue2kWMx9R8HynFLLIeN1fyAU?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>📋Create an Issue Type Screen Scheme</h4>
<ul>
<li>Associate Screens with Issue Operation: Create a ‘Bug Tracker Issue Type Screen Scheme’ and map the appropriate Screen Scheme to the Issue Type (i.e.,  ‘Bug’ and ‘Task’ ). The Issue Type Screen Scheme is associated to a project to define the issue layout. </li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfJ143ERfG6SR9HcerRIxkPNvT1Tj7BbO-xkRQVxWEXl8qHa1tULSfKgDs59Q8stnylSCKzn-m5vilWci-anQoxhNOebPBHpGcNY1AUQIyukPIXasQv-cRH6UQSD7cWVsg?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>📋Associate Screens to the Project</h4>
<ul>
<li>Now, go to the “Bug Tracker” project, then navigate to Project Settings → Screen. Change the currently assigned Issue Type Screen Schemes to a previously created  ‘Bug Tracker Issue Type Screen Scheme’  .</li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdUlv0ifdZyzfMo1lGvhlO6lsy1FiTiJwrcdg0hloDgvofA_WZJlXOfHx6mxCYp5hvE69RMhktHykrNtSYrh-DfdBkuO-x1PPTySe4LH_rEFC8HkTm5oEOg8aQY6SrmN9c?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<p></p>
<h3>🖋 Field Configuration</h3>
<p>Example Interaction: While creating a Bug or Task, the Bug Priority field must be filled.</p>
<h4>🖋 Create a new Custom Field</h4>
<ul>
<li>Go to Settings (⚙️) → Issues → Fields→Custom fields, and create new custom fields called "Bug Priority" by following the steps outlined in the <a href="https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/">article</a>. This will be visible in ‘Create_Screen’ and ‘View_Screen’ Screens created earlier. </li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXd4z9u416985XlMDcYnjpUTKtNmaVNFfmvpHy4PAw6M3e8iOxI7rymVW0iunzuGGmzOddAczCzRaGX9YOtzigsB-V4v-YZ7AvXYwIXZ23dGFgV6JMEIs9v8fWEAKUNsHQ?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>🖋 Create a new Field Configuration</h4>
<ul>
<li>Create a new Field Configuration ‘Bug Tracker Field configuration’ (easier approach is by copying the default one) and make sure the custom fields are the following. ;</li></ul>
<ul>
<li>Bug Priority is mandatory for all Bugs and Tasks.</li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfIgi_0Fd1sBGVsKsWcBMSaAOGI91z3IBiz9kSujOSD780efdOruqWvtO8pQRrX3XniTdc4RDyAw3L8OoMcrxhIWCSAPqUHc5wXWYXh59jdH1B3fPDhAek9mAol5zG7cxw?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeYPwz-q_1OBIhKz6Z-H6cYbLEXWABtYrGA3bQxBI_Ma9-Qgt3e1z7sz7n4rvVH9vl7d83asq0lN62ZSqPGgsuN7ew0HceYcxAvg38gRyMRlPkR_fXZ05bidk96iR-TOA?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>🖋 Create a new Field Configuration Scheme</h4>
<ul>
<li>Create a new Field Configuration Scheme ‘Bug Tracker Field Configuration Scheme’ and associate the “Bug Tracker Field configuration” Field configuration to the issue type Bug and Task. </li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcn9yWkzeSHq3zcrmxXLtR69qWQdjUl62p0Fh7byzd4RKNy3ra2XY97hMCO-7eOLnTw8V78ocvEQBUHxRVZHV-pH_ul2b2Z-V0per3p_sBot6--Ub4AeaEwuyVKkvRwiLw?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>🖋 Associate the Field Configuration Scheme to a Project</h4>
<ul>
<li>Now, go to the ‘Bug Tracker’ project, then navigate to Project Settings → Issues→ Fields change the currently assigned Field configuration scheme to a previously created ‘Bug Tracker Field Configuration Scheme’ . This makes Bug Priority custom field mandatory for issue type bugs. </li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfiFVa8yzW-LdJ9k9LtN94Br1WRg-eYjPeEtSAlaHq_73_yKrvDG6oRtbzfYA9hU3IcOPhYlX6cqGDKQPxwR2RRws9MViFaPLwy1RG_pAdpVPU6IZY7pCnO5JqjDMoeyw?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h3>📜 Permission Scheme</h3>
<p>Example Interaction: Only Project Administrator, Developer and QA Roles can transition as issue. </p>
<ul>
<li>Project Lead: Full Access</li>
<li>Developer: Full Issue and Comments Permissions</li>
<li>QA: Full Issue and Comments Permissions</li></ul>
<h4>📜Create a new Permission Scheme</h4>
<ul>
<li>Go to Settings (⚙️) → Issues → Permission Scheme, </li>
<li>Create a new Permission Scheme ‘Bug Tracker Permission Scheme’ (easier approach is by copying the default one) and make sure that only Developer and QA Roles can transition as issue. </li></ul>
<h4>📜Assign Permissions         </h4>
<p>The previous created QA and Developer Role have been granted Issue and Comments Permissions. Administrator Role has all permissions. Refer to the article<a href="https://confluence.atlassian.com/adminjiraserver076/managing-project-permissions-945111102.html"> ‘Managing Project Permissions’ </a>for more information. </p>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe8zkercQsRFiZVN-mwXT1VzZ3hW8X0n7FQ8Rz7gq3z6cQxqMtAMDsJEsyFgjVJKti1QcGaYdxl6Wv5L0woSoNR1HoGZjl0Pc2W3I4GFxmJsBPDt1Tpb4INBdImRhEQjts?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>📜Associate Permission Scheme to the Project </h4>
<ul>
<li>Associate a ‘bug tracker permission scheme’ to the ‘Bug Tracker’ project by navigating to Project Settings → Permissions. </li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeH0xsOBC4N_hSB5YcZJstRVQScrWxerGd-yAm53t2TaeB1_gDUfQ35EcGafKhIIWwnXscziaz2NNL5lgb4xxzg4CHJxKZ4iizMrkvAFf_mxD8QHB_j4-j22R11oRGQAj4?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h3>🔔 Notification Scheme</h3>
<p>Example Interaction: A notification is sent to the Project Lead, Reporter, Project Role (Administrators) and All Watchers when a new issue is created. Notify Assignee on issue assignment.</p>
<h4>🔔Create a new notification Scheme</h4>
<ul>
<li>Go to Settings (⚙️) → Issues → Notification Scheme, </li>
<li>Create a new Notification Scheme ‘Bug Tracker Notification Scheme’ (easier approach is by copying the default one) and update the Notification Scheme:</li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfaBCyJPqKRENF9zMi8iG-PF223U-GI194LbvRir7_G_rMoOJCnBfxHEEdxr3NXYqm911rYAjaTdT0qnoeyuj_YP6grjTl6K9QwxAgvYBXhK-DCrcY4TbNp0nDAemWc_A?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>🔔Add Notification Rules in the Scheme</h4>
<p>Add the following notification rules in the ‘Bug Tracker Notification Scheme’</p>
<ul>
<li>Notify Project Lead, Reporter, Project Role (Administrators)  and All Watchers when an issue is created.</li>
<li>Notify the Assignee when an issue is transitioned. </li></ul>
<p></p>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe_Qwtmq2I5qNxvrarkCQdmDcHN32EH9VF8OxzsVibO1h1JNtz8jDXiKMA1ynSiulPaBQLfaNT7G6_nIM4lWoYQ6Nc8jVp1qThRPSy8Y0pgpGGmMiqv1mBKWiWEDBqAON8?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>🔔Associate Notification Screen Scheme to the Project</h4>
<ul>
<li>Now, go to the ‘Bug Tracker’ project, then navigate to Project Settings → Notification→ Settings, change the currently assigned notification scheme to a previously created ‘Bug Tracker Notification Scheme’ . </li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdpUtbi645MPA1JVi9MB5DHca-03eru6z450KRS05Md2g0GM5iygnRH7dIgbyk2yVSozIdTSNd2cUaUW1xwMKicVdd7mjRSAwPN7QyP2QYcg8_sWFlOYkVqyjeZWPHc7y4?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h3>🔒 Security Scheme</h3>
<p>Example Interaction: Security vulnerabilities, need to be restricted to Administrator Role. </p>
<h4>🔒 Create a new Security Scheme</h4>
<ol start="1">
<li>Go to Settings (⚙️) → Issues → Issue Security Scheme, </li>
<li>Create a new Notification Scheme ‘Bug Tracker Issue Security Scheme’ (easier approach is by copying the default one) </li></ol>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcDKqmT7P4SPQOLP2_UNr-3A-4cjKg7i2HhQ7gSFTXIkT3irPpCywF_mg3ATRTR7JC7nHRPZOy2lbrA3F_r0pfMlNUCXnC3w-Y4_HIAFai9qPKZ84pGkWBz3JNAweLEZg?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>🔒Update the Security Scheme</h4>
<p>Add Security Levels:</p>
<ul>
<li>No Restriction (Default): Visible to all project members. This should be the default one. </li>
<li>Restricted: Visible only Administrators roles .</li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeP0ph2506NjT3nTE_GQYOCE4SVnR2w7EerfgP1kNKDm4fMD27n6cEvGjLAyTHY6BaG1ic-igj8zLFWxbZQjihgkAyE8j2Rz4Yt0xzl5WaaDBccJujESTnSJs4B53-Ti3Q?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>🔒Associate the Security Scheme to Project</h4>
<ul>
<li>Now, go to the ‘Bug Tracker’ project, then navigate to Project Settings →Security→, change the currently assigned security scheme to a previously created ‘Bug Tracker Issue Security Scheme’ .</li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeQg6q7ygSj5oWmXDJVJ5deUtEZyR4Pt5LanALwpzX7xCI_NKgVgH0IaNY0R-j4x-xffVqlekiqd2dMKenst-GjzmuCCoWk8Q7cZ3K95Fkhl_y0RCXjrB5Zi1ZCjlMFyg?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h3>🎨 Priorities Scheme</h3>
<p>Example Interaction: The Project has only 3 Priorities.; High, Medium, Low (Pre-existing)</p>
<h4>🎨 Create a new Priority Scheme</h4>
<ul>
<li>Create a new Priority Scheme ‘Bug Tracker Priority Scheme’ by following the <a href="https://support.atlassian.com/jira-cloud-administration/docs/manage-priority-schemes/">'Manage priority scheme's</a> article.</li>
<li>Associate the available Priorities to the ‘Bug Tracker Priority Scheme’. </li></ul>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfPmpYxMKmuv9WhWjZaahLo1QfAaBgMwuXQK-aPaRokiyeWimOxDrzBPAOiEeOyzDG31UgH8RD_MHfZ86aEqwFbPJdL1-tHsy6g-CyFDa0eeS1tu53stdeVTRXCZHizw6o?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<h4>🎨 Associate the Priority Scheme to the Project</h4>
<p>Add the ‘Bug Tracker Priority Scheme’ to ‘Bug Tracker’ Project from the Priority schemes pages. </p>
<p><img alt="" src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfjoSQHD4PjEzqfD2jlfanyEB5YUqTWJPqeI6BWbjxriZlNDSFjQQ_lj5BpEYaiydPEgFpEzDn0MMGFHOtlkcGN-UWIpIjf0nf7tRmo_OrPi7oFeTDahwKv3eHTKs4p7A?key=UD7TJ8OdiB7fOqKjKG7w8zmo" title=""></p>
<hr>
<p></p>
<p></p>
