# SOCKS
Cyber attacks can occur at any time requiring a security operations center to be manned at all times to combat the threats they pose to an organization's IT assets. **SOCKS (Security Operations Center Kick-ass Scheduler)** enables SOC managers in a 24x7 environment to easily schedule and track employees to ensure all shifts and mandatory roles are covered.

## Installation
Install [Docker](https://docs.docker.com/get-docker/)

Install git

Clone the repository:
```bash
git clone https://github.com/groth001/socks
```

Run the following commands:
```bash
docker-compose build
docker-compose run django bash
python3 manage.py migrate
python3 manage.py createsuperuser
exit
```

## Getting Started
To run SOCKS:
```bash
docker-compose up
```

# License
[GNU General Public License v3.0](https://github.com/groth001/socks/blob/master/LICENSE)

## User Stories
1. As a SOC subordinate employee, I want to view my team's shift and role assignments, so I know what to work on and when.   

   Acceptance Criteria:
   * A SOC employee can view the shift and role assignments for that employee's assigned team by selecting a day from the calendar.

2. As a SOC team lead, I want to assign my subordinates to shifts and roles, so I can ensure delivery of service at required times.

   Acceptance Criteria:
   * A SOC team lead can assign subordinate employees to a shift.
   * A SOC team lead can define roles for that lead's team and optionally set them as required.
   * A SOC team lead can assign employees on a shift to a role manually or randomly.
   * Manually assigned roles can be edited by the team lead until the end of the shift.

3. As a SOC team lead, I want to receive notifications of empty shift/role assignments so I can fill any gap in coverage.

   Acceptance Criteria:
   * The application sends an email to a SOC team lead when a shift has no available employee assigned and/or if a no employee on a shift is assigned to a required role for that lead's team.

4. As a SOC employee/team lead, I want to view shift/role assignments of other teams so I know who is available for cross-team collaboration.

   Acceptance Criteria:
   * Any user can select the calendar for another team and view the shift and role assignments for any day.

5. As a SOC team lead/supervisor, I want to view metrics of shift/role assignments so I can better understand how teams are operating.

   Acceptance Criteria:
   * Managerial employees are able to view weekly, monthly, and yearly reports in the app detailing shift metrics.
   * The app emails reports to managerial employees.

## Misuser Stories:
1. As a disgruntled employee, I want to alter future shift and role assignments, so I can cause schedule coverage gaps.

   Mitigation Criteria:
   * Authenticated users are given the minimum level of write permissions required for their access of the web app.
   * Only managerial users can edit future shift and role assignments.
   * Team leads cannot edit shift and role assignments for other teams.

2. As a lazy employee, I want to alter past shift and role assignments to make it look like I did more work.

   Mitigation Criteria:
   * Authenticated users are given the minimum level of write permissions required for their access of the web app.
   * Users cannot edit the shift and role assignments for past days.

3. As a malicious external hacker, I want to inject malicious code into the app, so I can gain access to the underlying system.

   Mitigation Criteria:
   * Proper validation is performed at all points of user input.
   * App components are contained within docker.

## Diagrams

### GUI Mockup
![Schedule GUI Mockup](https://github.com/groth001/socks/blob/master/img/socks_gui_mockup_schedule.JPG)

![OOO GUI Mockup](https://github.com/groth001/socks/blob/master/img/socks_gui_mockup_ooo.JPG)

![Assign GUI Mockup](https://github.com/groth001/socks/blob/master/img/socks_gui_mockup_assign.JPG)

![Reports GUI Mockup](https://github.com/groth001/socks/blob/master/img/socks_gui_mockup_reports.JPG)

### Architecture Diagrams
![System Context Diagram](https://github.com/groth001/socks/blob/master/img/socks_architecture_system_context.JPG)

![Containers Diagram](https://github.com/groth001/socks/blob/master/img/socks_architecture_containers.JPG)

![Components Diagram](https://github.com/groth001/socks/blob/master/img/socks_architecture_components.JPG)
