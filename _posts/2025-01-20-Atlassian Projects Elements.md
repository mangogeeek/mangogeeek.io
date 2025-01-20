## Table of Content
<body>
<nav id="TOC" role="doc-toc">
<ul>
<li><a href="#support-project-types"
id="toc-support-project-types">Support Project Types</a></li>
<li><a href="#workflow-representation-of-jira-elements"
id="toc-workflow-representation-of-jira-elements">Workflow
Representation of JIRA Elements</a></li>
<li><a
href="#comprehensive-guide-to-jira-project-creation-and-modification-example-based-learning"
id="toc-comprehensive-guide-to-jira-project-creation-and-modification-example-based-learning">Comprehensive
Guide to JIRA Project Creation and Modification (Example-Based
Learning)</a></li>
<li><a href="#create-a-project" id="toc-create-a-project">📂 Create a
Project</a></li>
<li><a href="#configure-project-roles."
id="toc-configure-project-roles.">🧑‍🤝‍🧑 Configure Project Roles.</a></li>
<li><a href="#customizing-schemes-for-the-project"
id="toc-customizing-schemes-for-the-project">📋 Customizing Schemes for
the Project</a>
<ul>
<li><a href="#issue-type-scheme" id="toc-issue-type-scheme">🧩 Issue
Type Scheme</a></li>
<li><a href="#workflow-scheme" id="toc-workflow-scheme">🛠 Workflow
Scheme</a></li>
<li><a href="#screen-scheme" id="toc-screen-scheme">📋 Screen
Scheme</a></li>
<li><a href="#field-configuration" id="toc-field-configuration">🖋 Field
Configuration</a></li>
<li><a href="#permission-scheme" id="toc-permission-scheme">📜
Permission Scheme</a></li>
<li><a href="#notification-scheme" id="toc-notification-scheme">🔔
Notification Scheme</a></li>
<li><a href="#security-scheme" id="toc-security-scheme">🔒 Security
Scheme</a></li>
<li><a href="#priorities-scheme" id="toc-priorities-scheme">🎨
Priorities Scheme</a></li>
</ul></li>
</ul>
</nav>
<p> </p>
<hr />
<h2 id="support-project-types">Support Project Types</h2>
<table>
<tbody>
<tr>
<td><p>Product Name</p></td>
<td><p>Project Type</p></td>
<td><p>Unique Issue Types</p></td>
<td><p>Standard Issue Types</p></td>
<td><p>Management Type</p></td>
</tr>
<tr>
<td><p>Jira Product Discovery</p></td>
<td><p>Product Discovery</p></td>
<td><p>Ideas</p></td>
<td><p>Task, Sub-task</p></td>
<td><p>Team-managed only</p></td>
</tr>
<tr>
<td><p>Jira Service Management</p></td>
<td><p>Service Management</p></td>
<td><p>Request, Incident, Problem, Change, Service Request</p></td>
<td><p>Task, Sub-task, Custom Request Types</p></td>
<td><p>Company and Team-managed</p></td>
</tr>
<tr>
<td><p>Jira</p></td>
<td><p>Software Projects</p></td>
<td><p>Epic, Story, Bug</p></td>
<td><p>Task, Sub-task</p></td>
<td><p>Company and Team-managed</p></td>
</tr>
<tr>
<td><p>Jira Work Management</p></td>
<td><p>Business Projects</p></td>
<td><p>None</p></td>
<td><p>Task, Sub-task</p></td>
<td><p>Company and Team-managed</p></td>
</tr>
</tbody>
</table>
<hr />
<h2 id="workflow-representation-of-jira-elements">Workflow
Representation of JIRA Elements</h2>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdTUpR6JmZsgR_0skFtzNUs8GjMyoVwOqze_cjc1chtgcbZCyi796TYF37RG6AHDM0jem600-X5dN7h_2Pe1W69E1BnWSEKpcMYnMxnZf635dUVYJt4utkXo9QoUb5omPg?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h2
id="comprehensive-guide-to-jira-project-creation-and-modification-example-based-learning">Comprehensive
Guide to JIRA Project Creation and Modification (Example-Based
Learning)</h2>
<p>Let’s set up a company managed Jira project for a software
development team. The goal is to manage (Bugs and Tasks) Issue Types ,
ensuring that issues move through their respective workflows, fields are
configured correctly, and notifications reach the right people.</p>
<ul>
<li>Setup Objective: Configure schemes for Issue Types, Workflows,
Screens, Fields, Permissions, Security, and Notifications.</li>
<li>Practical Use: Log Bugs and Tasks, track their progress through
workflows, notify relevant team members.</li>
</ul>
<table>
<tbody>
<tr>
<td><p>Element</p></td>
<td><p>Mapping</p></td>
<td><p>Explanation</p></td>
</tr>
<tr>
<td><p>Issue Type Scheme</p></td>
<td><p>Project → Issue Type Scheme → Issue Types</p></td>
<td><p>Defines the types of issues (e.g., Bug, Task, Story) available in
the project.</p></td>
</tr>
<tr>
<td><p>Workflow Scheme</p></td>
<td><p>Project → Workflow Scheme → Workflows</p></td>
<td><p>Controls the lifecycle (statuses and transitions) for each issue
type.</p></td>
</tr>
<tr>
<td><p>Screen Scheme</p></td>
<td><p>Project → Issue Type Screen Scheme → Screen Schemes →
Screens</p></td>
<td><p>Defines the fields displayed at different issue stages (Create,
Edit, View screens).</p></td>
</tr>
<tr>
<td><p>Field Configuration</p></td>
<td><p>Project → Field Configuration Scheme → Field Configuration →
Custom Fields</p></td>
<td><p>Controls the behavior (required, optional, hidden) of fields in
the project.</p></td>
</tr>
<tr>
<td><p><a
href="https://confluence.atlassian.com/adminjiraserver076/managing-project-permissions-945111102.html">Permission
Scheme</a></p></td>
<td><p>Project → Permission Scheme → Roles and Users/Group</p></td>
<td><p>Defines who can perform specific actions (e.g., create, edit,
transition issues).</p></td>
</tr>
<tr>
<td><p>Notification Scheme</p></td>
<td><p>Project → Notification Scheme</p></td>
<td><p>Configures notifications for issue events (e.g., issue creation,
status changes).</p></td>
</tr>
<tr>
<td><p>Security Scheme</p></td>
<td><p>Project → Issue Security Scheme → Security Levels →
Roles/Users/Groups</p></td>
<td><p>Restricts visibility of specific issues to selected roles or
users.</p></td>
</tr>
<tr>
<td><p>Priorities Scheme</p></td>
<td><p>Settings (⚙️) →Priorities → Priority schemes</p></td>
<td><p>Defines the priority levels (e.g., Low, Medium, High, Critical)
that can be assigned to issues.</p></td>
</tr>
<tr>
<td><p>Project Roles</p></td>
<td><p>Project → Project Roles → Users/Group</p></td>
<td><p>Assigns roles (e.g., Developer, Tester) to users or groups for
project-specific permissions.</p></td>
</tr>
<tr>
<td><p>Issue Features</p></td>
<td><p>Project → Issue Features</p></td>
<td><p>Adds specific functionalities to issues like linking, time
tracking.</p></td>
</tr>
<tr>
<td><p>Issue Attributes</p></td>
<td><p>Project → Issue Attributes</p></td>
<td><p>Defines the characteristics of issues like Statutes and
Resolution.</p></td>
</tr>
<tr>
<td><p>Project Components</p></td>
<td><p>Project → Components</p></td>
<td><p>Breaks down the project into logical modules or areas (e.g.,
Frontend, Backend).</p></td>
</tr>
<tr>
<td><p>Project Versions</p></td>
<td><p>Project → Versions</p></td>
<td><p>Tracks versioned releases or milestones (e.g., v1.0, v2.0) for
the project.</p></td>
</tr>
<tr>
<td><p>Project Category</p></td>
<td><p>Project → Category</p></td>
<td><p>Groups related projects under a category (e.g., Internal
Projects, Client Projects).</p></td>
</tr>
<tr>
<td><p>Automation Rules</p></td>
<td><p>Project → Automation Rules</p></td>
<td><p>Automates repetitive tasks (e.g., auto-assigning issues, sending
reminders for due dates).</p></td>
</tr>
</tbody>
</table>
<hr />
<h2 id="create-a-project">📂 Create a Project</h2>
<p>Follow the steps outlined in <a
href="https://support.atlassian.com/jira-software-cloud/docs/create-a-new-project/">“Create
a new project”</a> link to create a <a
href="https://support.atlassian.com/jira-software-cloud/docs/what-are-team-managed-and-company-managed-projects/">company
managed project</a> named ‘Bug Tracker’.</p>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfFgU-akt0_RD2iyebUqi-CDPEDX0TWNdWKaTZhNN3qFv9ugCIVDHgkPQ4bY135A35SeNvc18h5eWnAkmm4WDLCRHMwY3i8NkuDF1PHtKUxFqrB4gFmCpsWTqyHUhRm0mg?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXei1kPzIioROXUvRUDAS4aWp6P-sS_CHjkBIYwqoSKl61p4kG-_p8FJLmUKKKvq_A1zDPt8B0LKnIdkqm_GWSBGe6E8CAD4bcd5K8oMEnUxCHRzAGL_WkgOzdRGORG_ke4?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<hr />
<h2 id="configure-project-roles.">🧑‍🤝‍🧑 Configure Project Roles.</h2>
<h4 id="add-project-roles">🧑‍🤝‍🧑Add Project Roles</h4>
<ul>
<li>Navigate to Project Settings →People. Assign roles to users or
groups. Make sure these roles are already created, if not, follow the <a
href="https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/">article</a>.</li>
</ul>
<ul>
<li>Administrator: Bella Gibson (Product Lead)</li>
<li>Developer: Harry Young</li>
<li>QA: Owen Black</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeXmB06BFrFQeer_uRKCLRjep4cBBUrYXDvzCNOnB-ot1ni_NQzgXbRZyGm5p_t6JnbT54n8cn_xeuN8s6W82l54Q5ubb-8P-OrrxXeROMMtpvX4Il74DgDVG3VEPzU8-U?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<hr />
<h2 id="customizing-schemes-for-the-project">📋 Customizing Schemes for
the Project</h2>
<h3 id="issue-type-scheme">🧩 Issue Type Scheme</h3>
<ul>
<li>Custom Issue Type Scheme: ‘Bug Tracker Issue Type Scheme’</li>
<li>Custom Issue Types: Bug, Task, Improvement</li>
<li>Associate the scheme with the ‘Bug Tracker” project.</li>
</ul>
<p>Example Interaction: QA and Developer log Bugs &amp; Tasks issue for
a software defect.</p>
<h4 id="creating-a-scheme">🧩Creating a Scheme</h4>
<ul>
<li>Go to Settings (⚙️) → Issues → Issue Types → Issue type schemes. Add
a new issue type scheme named ‘Bug Tracker Issue Type Scheme’ by
following the steps in the <a
href="https://support.atlassian.com/jira-cloud-administration/docs/add-edit-and-delete-an-issue-type-scheme/">article</a>.</li>
<li>Add Bug and Task.</li>
<li>Remove other issue types i (e.g., Epic, Story, Sub-task, if not
required).</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe1EEvxjHMGgTeFzp7N2udRoREQkhHzLzMBWEHmh-A5JqXiEJjCXdj_fDkBnwAx8LbcrkbETe7e04Brv_tnAu2mlvfyro1QQJbRopRwY8HwEldWEMSUlStRCPX9dVOiGHM?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="associating-scheme-with-the-project">🧩Associating Scheme with
the Project</h4>
<p>Now, go to the ‘Bug Tracker’ project, then navigate to Project
Settings → Issue → Types. Change the currently assigned Issue Type
scheme to a ‘Bug Tracker Issue Type Scheme’ scheme.</p>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXd7pRwsV91LvaF2jJ5zBMIZIkU-P3T0Qpr2i4h2KkTw3vh1i96Tc0KYVP6NXtiF0vjqssJelEh-f-VBJTA7N1vrxaHmPndYBzbCB-uYjhTVIcTtmRqQkdBMWNZcniYJBL4?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<p>Note → We will take care of Workflow, Field Configuration and Screen
mapping to Issue Type Screen in the later steps.</p>
<h3 id="workflow-scheme">🛠 Workflow Scheme</h3>
<p>Example Interaction: An Issue moves through the defined workflow,
transitioning from ‘Open → In Progress → In QA → Done.’</p>
<h4 id="create-a-workflow">🛠 Create a Workflow</h4>
<ul>
<li>Go to Settings (⚙️) → Issues → Workflows, and create new workflows
called ‘Bug and Task Workflow’ by following the steps outlined in the <a
href="https://support.atlassian.com/jira-work-management/docs/how-to-create-workflows/">article</a>.</li>
</ul>
<ul>
<li>For Bugs: States: Open → In Progress → In QA → Done.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfBzsLzG1QQE1SEE43dKhK9ceiHqciqaNYTtiZpimiDVd018NNCp5T_dxUwsE33c8nQhYM1I_d_8MB1iO5_x0XQFv4lt5HBSBxwr7hk4QMgg3952_OQZWFJXfmjRG2KEjg?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<ul>
<li>Transitions: For ‘Bug and Task Workflow’. Restrict the transition to
‘Done’ only for QA roles. To know more about transition, read the <a
href="https://support.atlassian.com/jira-cloud-administration/docs/work-with-issue-workflows/">article</a>.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfsAmpZ0VJbBKir-nEjtVF0v7p_Lbj575jM9yF4dtt_djNWFlWIhqdbbLB7jXtYnixzhA7tgQtJdzSElFYLHKXYxFWcdBlAcpcBUOSyxWqT79GcgdxE5CHTBWTx0KLbYHA?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="create-a-workflow-scheme">🛠 Create a Workflow Scheme</h4>
<ul>
<li>Next, create a new workflow scheme named ‘Bug Tracker Workflow
Scheme’ and add ‘Bug and Tasks Workflow’ for the ‘Bug’ and ‘Task’ issue
types.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfEkoWsC5c7ZBrYbqiMsambteKaVhzHTJeLA08bU6_QcQbkQuNcSNl2IfxypPx1SjUfbO0FgsUVS_0a28PnXFp8FWy_nvfotZN8L6AltD6tXJjZk9AMpLDcW3OU8pksnmQ?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="associate-the-workflow-scheme-to-project">🛠 Associate the
Workflow Scheme to Project</h4>
<ul>
<li>Now, go to the ‘Bug Tracker’ project, then navigate to Project
Settings → Workflows. Switch the currently assigned Workflow scheme to
the ‘Bug Tracker Workflow Scheme’ .</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcMu97v1lXa0MRdOo0vN21BRhxXxn7ZHPM9cIKVj1AYI1AYZVo5ENCzs2vTVKay-zrEwktmNswjaKl2uxSPUW1nIh0ybPOkrE3DxT-S3Qyvuzc1QBOxaNDKqk5kDrpBpzI?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h3 id="screen-scheme">📋 Screen Scheme</h3>
<p>Example Interaction: The Bug Create Screen shows Summary,
Description, and Priority, while the Edit Screen allows adding
Assignee.</p>
<h4 id="create-screens">📋Create Screens</h4>
<ul>
<li>Go to Settings (⚙️) → Issues → Screens → Screens, and create new
screens A screen is an arrangement of fields that are displayed when the
issue is created, edited or transitioned through workflow. Define
screens as the following. :</li>
</ul>
<ul>
<li>Create_Screen: Fields like Summary, Description, Priority.</li>
<li>Edit_Screen: Add fields like Assignee and Labels.</li>
<li>View_Screen: Show all fields.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcmrcUSZKRv1TyE8JOrydwaB9ONK48FpDNWQdVbv9fyPmDByibYdGlrPiprdgzBL9_qtDK38YEDXO-27hTppMSz4RhhjEVRSOP_OsOhPw5anH_y6lXAUIuLZn2oflZYgTM?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="create-a-screen-scheme">📋Create a Screen Scheme</h4>
<ul>
<li>Create a new Screen Schemes called ‘Bug Tracker Screen Scheme’ by
following the steps outlined in the <a
href="https://support.atlassian.com/jira-cloud-administration/docs/configure-issue-screens/">article</a>
and create an Issue Operation mapping with previously created screen.
This configuration decided which screen will be displayed for each issue
operation.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcqXa9T8BdJ5RnuPXBOVuh0ZV0SfKJ2WvDON_SwKFAr4Qz2IOFI8Lrq0-N-Tspu2JaTSjk4gt5EvvUKzCnIl_tJ5O4GeH6iVywvreSst-f9Bp2CEDzk1AStIsdnfaZNpgc?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="create-an-issue-type-screen-scheme">📋Create an Issue Type
Screen Scheme</h4>
<ul>
<li>Associate Screens with Issue Operation: Create a ‘Bug Tracker Issue
Type Screen Scheme’ and map the appropriate Screen Scheme to the Issue
Type (i.e., ‘Bug’ and ‘Task’ ). The Issue Type Screen Scheme is
associated to a project to define the issue layout.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXc8spXojOS9oBSHVKE70H2s968Y9ANa9Ig-qzotCJu3EsOzXK8x4supN66Snw3WEWJbNBdpiAkvSQk5cXK08buZKTQs_YYOGVryUmmbH7x-0r2bDaeHQSENskuafAYjTPs?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="associate-screens-to-the-project">📋Associate Screens to the
Project</h4>
<ul>
<li>Now, go to the “Bug Tracker” project, then navigate to Project
Settings → Screen. Change the currently assigned Issue Type Screen
Schemes to a previously created ‘Bug Tracker Issue Type Screen Scheme’
.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeMmZKhESUDDCYyeGckwaSb3VUn7s2rU48TT_65RJj9uAgt-pXcpANP1fJrvm7sSzLj4b_0-a2Z29lmk_MG9bDcdUpfMT0D1KTHk1tS2QDv0uGO2FL78tDgLYuJFdBzvrw?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h3 id="field-configuration">🖋 Field Configuration</h3>
<p>Example Interaction: While creating a Bug or Task, the Bug Priority
field must be filled.</p>
<h4 id="create-a-new-custom-field">🖋 Create a new Custom Field</h4>
<ul>
<li>Go to Settings (⚙️) → Issues → Fields→Custom fields, and create new
custom fields called "Bug Priority" by following the steps outlined in
the <a
href="https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/">article</a>.
This will be visible in ‘Create_Screen’ and ‘View_Screen’ Screens
created earlier.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfQWeV0QmqkitKp7gPaeazHYjiWHqET5W9ABLm57GneVY7DhV9oDfN7EtfM0u5Xf24JMLhlJiwFi9vcGx3AtMoKTMFq3f-uLplH8q5fFzBqHB7EhNt277i7uW3J5BJ8HA?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="create-a-new-field-configuration">🖋 Create a new Field
Configuration</h4>
<ul>
<li>Create a new Field Configuration ‘Bug Tracker Field configuration’
(easier approach is by copying the default one) and make sure the custom
fields are the following. ;</li>
</ul>
<ul>
<li>Bug Priority is mandatory for all Bugs and Tasks.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdyZ-NmabGeeW9bY5KvKJ-i4UsKy5dAvFpZzpR5MEQ311UfTjoMXIv5KHtouFCN5wkt0SWu77MmPvte4nZvhQvNl4g3uOZ3O3SGGhaMk3FkFEV29be13Y7DEEXyiPX-gas?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdz1blSES8odsgqrHyjEWn38FyYTw0aoTR1ovwIenrXFBAKCdSWxQsrXrfEJnVoLdkp81XIpUknhRrukyyt935WqLmXLetBSfZGvxRscF-iyTx38AH6J5Bw-5XC0PR58A?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="create-a-new-field-configuration-scheme">🖋 Create a new Field
Configuration Scheme</h4>
<ul>
<li>Create a new Field Configuration Scheme ‘Bug Tracker Field
Configuration Scheme’ and associate the “Bug Tracker Field
configuration” Field configuration to the issue type Bug and Task.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXc6iwT1CCgoPcC4JMomSFAVUjoT9Cl2pzOxePrZb1mxpFXA6hAKouoySxMSL_i3c-IGVHOxsq--0640lExpPMjMpTb35NaTUwg0Y-y5g4rpA2Goy1HfK7NnSrjPwWbEt9c?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="associate-the-field-configuration-scheme-to-a-project">🖋
Associate the Field Configuration Scheme to a Project</h4>
<ul>
<li>Now, go to the ‘Bug Tracker’ project, then navigate to Project
Settings → Issues→ Fields change the currently assigned Field
configuration scheme to a previously created ‘Bug Tracker Field
Configuration Scheme’ . This makes Bug Priority custom field mandatory
for issue type bugs.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfonFGfaAJFuEf5gqyJWMBqGC-GTbQaihKv4KDPsMud7fPcNMCYLMdpQocorp5zhP6g1TkkDV0vVhRdkCnm9YdQ55RuPNxPPx1hqlc2SuKhg_mfx2PG8x4uRGKzW_JX-A?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h3 id="permission-scheme">📜 Permission Scheme</h3>
<p>Example Interaction: Only Project Administrator, Developer and QA
Roles can transition as issue.</p>
<ul>
<li>Project Lead: Full Access</li>
<li>Developer: Full Issue and Comments Permissions</li>
<li>QA: Full Issue and Comments Permissions</li>
</ul>
<h4 id="create-a-new-permission-scheme">📜Create a new Permission
Scheme</h4>
<ul>
<li>Go to Settings (⚙️) → Issues → Permission Scheme,</li>
<li>Create a new Permission Scheme ‘Bug Tracker Permission Scheme’
(easier approach is by copying the default one) and make sure that only
Developer and QA Roles can transition as issue.</li>
</ul>
<h4 id="assign-permissions">📜Assign Permissions</h4>
<p>The previous created QA and Developer Role have been granted Issue
and Comments Permissions. Administrator Role has all permissions. Refer
to the article <a
href="https://confluence.atlassian.com/adminjiraserver076/managing-project-permissions-945111102.html">‘Managing
Project Permissions’</a> for more information.</p>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXc4TcCSNSYJgpSQsRGnCnTN4AX2yhZ5oz9AtZ3U6flc4cM23-4t9uWl7xYzXsTHsfwsQ4vxGb_j8QQqLGC9th_U8Y5RxLL1BFOHebTP9h9LBlyu_vu4zpKPC4Xg_wMLg04?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="associate-permission-scheme-to-the-project">📜Associate
Permission Scheme to the Project</h4>
<ul>
<li>Associate a ‘bug tracker permission scheme’ to the ‘Bug Tracker’
project by navigating to Project Settings → Permissions.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcOGExxkyI8JhPLCb1Ty0NeYrx0M_6Eg8R0BZhOuOHaHJs3aQ6qwVpgBwDpJZvq_XgZSaRy11zrAoGQ_KQsXRJbOWeICZwpWX2JZfzzBtC5GUQP2K_DGkN_VluaqkM8UcI?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h3 id="notification-scheme">🔔 Notification Scheme</h3>
<p>Example Interaction: A notification is sent to the Project Lead,
Reporter, Project Role (Administrators) and All Watchers when a new
issue is created. Notify Assignee on issue assignment.</p>
<h4 id="create-a-new-notification-scheme">🔔Create a new notification
Scheme</h4>
<ul>
<li>Go to Settings (⚙️) → Issues → Notification Scheme,</li>
<li>Create a new Notification Scheme ‘Bug Tracker Notification Scheme’
(easier approach is by copying the default one) and update the
Notification Scheme:</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXc8VCmfSdH2t2yqEGNDzf7d0hYLwWHF4hmqB6DH9sQZTWpXN-Wm9Y1Rq_iFA6hPMI1eNRqqGS1PuvV-tC3MTWAsX8GOfFNNaRa8nleVgJ79Q2QzK-qt8lEjkyLXUzzlVg?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="add-notification-rules-in-the-scheme">🔔Add Notification Rules
in the Scheme</h4>
<p>Add the following notification rules in the ‘Bug Tracker Notification
Scheme’</p>
<ul>
<li>Notify Project Lead, Reporter, Project Role (Administrators) and All
Watchers when an issue is created.</li>
<li>Notify the Assignee when an issue is transitioned.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdfEDNmtPaxFXQVwDPvU_mlCbxxl8IHhNdnyqZOOSwzeMOsSDP2976_MoEQ1bsxRgC9RolYrjP1ekd-IGX_E4hKCrDVyKip_pEgKlYRiQWMnx7G3NlZbe4UN4GV9tRsZZ4?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="associate-notification-screen-scheme-to-the-project">🔔Associate
Notification Screen Scheme to the Project</h4>
<ul>
<li>Now, go to the ‘Bug Tracker’ project, then navigate to Project
Settings → Notification→ Settings, change the currently assigned
notification scheme to a previously created ‘Bug Tracker Notification
Scheme’ .</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXciuUetlpoCmBhsm3DCc7KvNFHpXPjFADewBCswPvzJDe7TiJea6c_amL_ZKl3HHf_jWE8ONAzpdAaOjRgsBUTu1Bu3OGDq6fw48mu8NQQq4CyCPlHPoTqCZgKrfLnlE3c?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h3 id="security-scheme">🔒 Security Scheme</h3>
<p>Example Interaction: Security vulnerabilities, need to be restricted
to Administrator Role.</p>
<h4 id="create-a-new-security-scheme">🔒 Create a new Security
Scheme</h4>
<ol>
<li>Go to Settings (⚙️) → Issues → Issue Security Scheme,</li>
<li>Create a new Notification Scheme ‘Bug Tracker Issue Security Scheme’
(easier approach is by copying the default one)</li>
</ol>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeSzudwSxnJAMHZ26o47nyHhia15ovkoG5c1IpuKQZMP8kabyFH36yQyWRqYxyOCcKhR_PKy9mJ5jKCXDehcqrfEz2VoJHBaytH8YsJaMCltHxKnoT9347SvWMZv6PfmQ?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="update-the-security-scheme">🔒Update the Security Scheme</h4>
<p>Add Security Levels:</p>
<ul>
<li>No Restriction (Default): Visible to all project members. This
should be the default one.</li>
<li>Restricted: Visible only Administrators roles .</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXc3CaINqGC4oUDTTIp7360YuTnQbbpMSKAbLtFLugvVTG3HG0Clk4owa-aOyQ2t0HT0AeWsCNYkcTN3ClRueSd8maS433WqwiLdBPS-qLQBjUeUy8DiKilcyiuk_JxyAaE?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="associate-the-security-scheme-to-project">🔒Associate the
Security Scheme to Project</h4>
<ul>
<li>Now, go to the ‘Bug Tracker’ project, then navigate to Project
Settings →Security→, change the currently assigned security scheme to a
previously created ‘Bug Tracker Issue Security Scheme’ .</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdsKvboXU4xxMVup7Xm5rLLakn2qyRWfYoo0Vv0pP456J9xH12yxssbaAt0nyy8jVh28JQKJ1wXT9vjMUhNjrx1hBobc2TdXz7W9p4eywGgHBwtjGRMKxiFnKVuVnHkcg?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h3 id="priorities-scheme">🎨 Priorities Scheme</h3>
<p>Example Interaction: The Project has only 3 Priorities.; High,
Medium, Low (Pre-existing)</p>
<h4 id="create-a-new-priority-scheme">🎨 Create a new Priority
Scheme</h4>
<ul>
<li>Create a new Priority Scheme ‘Bug Tracker Priority Scheme’ by
following the <a
href="https://support.atlassian.com/jira-cloud-administration/docs/manage-priority-schemes/">'Manage
priority scheme's</a> article.</li>
<li>Associate the available Priorities to the ‘Bug Tracker Priority
Scheme’.</li>
</ul>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdHPFtc9VnDaCcGPCUf-6OGv1z89_Np2j4L6UrMisRSzMTM-tNPfDXCxRyZM-hlUUV7sdpMr2PIK1SfQlVViFpJKdwu6XFLTY8ddWAOsbYcZcef49nxSPEdv4t1KyaI5dk?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<h4 id="associate-the-priority-scheme-to-the-project">🎨 Associate the
Priority Scheme to the Project</h4>
<p>Add the ‘Bug Tracker Priority Scheme’ to ‘Bug Tracker’ Project from
the Priority schemes pages.</p>
<p><img
src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeLjRkoN1fMTju39a62DvXMWq8MnfCRcSC0IZSWPRmQBwT_yhK_5Eyw8Sdc-4fxATNesTEp0Mz4xyjvsKI9NlLHEsplLnZGaVgR5t0XTd4c6A9DrS_sm5wVSUaMeNujHA?key=UD7TJ8OdiB7fOqKjKG7w8zmo" /></p>
<hr />
</body>
</html>
