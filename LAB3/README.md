Lab 3 - Patient Vitals Alert & Monitoring App
Project Details
Project Title: Patient Vitals Alert & Monitoring App
Primary Domain: Healthcare & Patient Monitoring
Target Actors: Device / Sensor, On-Call Caregiver
Selected Architecture: Microservices Architecture


Final Submission Files
PES2UG24CS203_Component_Diagram.drawio - editable UML component diagram source.
PES2UG24CS203_Lab_3.pdf - exported component diagram PDF.
PES2UG24CS203_Architecture_Justification.pdf - PDF version of the architecture justification.

Component Diagram Coverage

The diagram contains 7 components representing the microservices-based patient monitoring system:

Microservices / Application Components
Telemetry Ingestion Service
Vitals Evaluation Engine
Alert & Escalation Service
Threshold Configuration Service
Alert Acknowledgement & Audit Service
Caregiver Dashboard Service
Data Component
Patient Vitals Database

The diagram shows how patient vital-sign telemetry is received, evaluated against configured thresholds, converted into alerts, delivered to caregivers, acknowledged, audited, and displayed through the caregiver dashboard.

Interfaces and Data Flow

The diagram includes labelled provided/required interfaces and assembly connectors representing the communication between services.

Key interfaces and data flows include:

DeviceTelemetry - Device / Sensor provides patient telemetry to the Telemetry Ingestion Service.
TelemetryIngest - Telemetry Ingestion Service sends ingested telemetry to the Vitals Evaluation Engine.
AlertTrigger - Vitals Evaluation Engine communicates alert conditions to the Alert & Escalation Service.
NotificationDispatch - Alert & Escalation Service dispatches notifications to the Caregiver Device using Push / SMS.
ThresholdConfig / AlertTrigger - Threshold Configuration Service provides threshold information and alert-related configuration to the Vitals Evaluation Engine.
AcknowledgeAlert - Caregiver Dashboard Service communicates caregiver alert acknowledgements to the Alert Acknowledgement & Audit Service.
PatientProfile - Patient profile information is accessed between the Threshold Configuration Service and Patient Vitals Database.
AuditWrite - Alert Acknowledgement & Audit Service writes audit information to the Patient Vitals Database.
VitalsQuery - Caregiver Dashboard Service retrieves patient vital information from the Patient Vitals Database.
DashboardView - Caregiver Dashboard Service provides the monitoring dashboard view to the On-Call Caregiver.
Architecture Characteristics

The diagram follows a Microservices architectural style, where individual responsibilities are separated into independent services. Each service focuses on a specific function such as telemetry ingestion, vital evaluation, alert handling, configuration, auditing, or dashboard presentation.

The diagram uses black, white, and line styling only, with no decorative colours. It includes UML component notation, provided and required interfaces, assembly connectors, labelled communication paths, and a system boundary labelled "Vitals Monitoring System".

Architecture Justification Coverage

The architecture justification includes:

Scenario review of the patient vitals monitoring system
Comparison of Microservices, Layered, and Client-Server architectural styles
Selected architecture: Microservices
Scenario-specific reasons for selecting Microservices
Security advantages of service separation and access control
Performance and scalability benefits for telemetry and alert processing
Component and interface responsibilities
Patient vitals database interaction
Alert notification and caregiver acknowledgement flow