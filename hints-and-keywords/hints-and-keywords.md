# Exam AZ-900: Microsoft Azure Fundamentals Hints and Keywords
I have finally passed my Exam AZ-900: Microsoft Azure Fundamentals with a score of 865 on June 2023. Here are some of things that helped me remember and understand AZ-900.

## Describe cloud concepts
### Describe cloud service types
| Service | Keywords | Products |
| --- | --- | --- |
| Infrastructure as a Service (IaaS) | **complete control of**: hardware, virtual machine (VM), networking | Azure VMs, Azure Disk Storage, Azure Virtual Networks (VNet) |
| Platform as a Service (PaaS) | provides ready-to-use environment, usually azure product with fancy names | Azure App Service, Azure SQL Database, Cosmos DB, Azure Files, Azure Active Directory Domain Services |
| PaaS Serverless | serverless, business logic priority | Azure Functions, Azure Logic App |

## Compute
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Virtual Desktop | **virtual desktop** service to access your desktop from anywhere, PaaS | Enable a secure, remote desktop experience from anywhere |
| Azure Dedicated Host | full **control** and strict **compliance**, physical virtualization hosts dedicated to individual customers | A dedicated physical server to host your Azure VMs for Windows and Linux |

## Networking
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure ExpressRoute | traffic does not route (traverse) the internet | Experience a fast, reliable, and **private** connection to Azure |
| VPN Gateway | encrypted traffic, point-to-site, site-to-site | Establish secure, cross-premises connectivity |
| Content Delivery Network | deliver videos and streaming | Fast, reliable content delivery network with global reach |
| Azure Arc |  simplifies governance and management by delivering a consistent multicloud and on-premises management platform | Secure, develop, and operate infrastructure, apps, and Azure services anywhere |
| Azure Traffic Manager | DNS-based traffic **load balancer**, distribute traffic to your public facing applications, for **global apps** | Route incoming traffic for high performance and availability |
| Azure Load Balancer | works with **network performance**, balance **traffic** within VMs, **global and regional apps** | Network-layer load balancer |
| Azure Application Gateway | works with **web front ends**, **regional apps** | Application delivery controller as a service |
| Azure Front Door | deliver real-time perfornace for **global apps** | Highly secure global application delivery |

## Databases
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Cosmos DB | **non-relational**, NoSQL database service, **high availability** | Build or modernize scalable, high-performance apps |
| Azure Database for MySQL | Microsoft-hosted version of the open source MySQL relational database | Fully managed, scalable MySQL Database |
| Azure Database for PostgreSQL | Microsoft-hosted version of the open source MySQL relational database | Fully managed, intelligent, and scalable PostgreSQL |
| Azure SQL Managed Instance | **lift-and-shift**, fully managed, up-to-date platform | Modernize SQL Server applications with a managed, always-up-to-date SQL instance in the cloud |

## Security
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Information Protection | encrypt documents and emails | Better protect your sensitive information—anytime, anywhere |
| Azure DDoS Protection | threats and attacks, network layer (OSI), perimeter layer (DiD) | Protect your Azure resources from distributed denial-of-service (DDoS) attacks |
| Microsoft Sentinel | **sentinel** definition: a soldier or guard whose job is to stand and keep watch, **SIEM**, **SOAR**, AI based security, response to threats just like a guard | Cloud-native SIEM and intelligent security analytics |  
| Azure Firewall | applied at **VNet level**, control traffic flow, network address translation (NAT), **filter** traffic across many VNets | Protect your Azure Virtual Network resources with cloud-native network security |
| Network Security Group (NSG) | **allow or deny**, connect using port, inbound/outbound rules, associated with VM **network interface controller (NIC)** and a **subnet** but not a VNet |  |
| Azure Key Vault | vault = to safekeep, secrets, keys | Safeguard and maintain control of keys and other secrets |
| Azure Active Directory (Azure AD) | providing authentication and authorization for users, MFA, conditional access, SSO | Synchronize on-premises directories and enable single sign-on |
| Azure Active Directory Domain Services | run legacy applications in the cloud that can't use modern authentication | Manage your **domain controllers** in the cloud |
| Microsoft Defender for Cloud | provides security policy, compliance manager, sercure score, security alerts, just-in-time (JIT) network access | Protect your multi-cloud and hybrid environments |
| Azure Front Door | application delivery network (ADN) service, operates at the geographic layer and is not regional | Modern cloud CDN that delivers optimized experiences to your users anywhere |
| Azure Active Directory External Identities |  you can share your resources and define how your internal users can access external organizations | Consumer identity and access management in the cloud |

## Containers
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Kubernetes Service (AKS) | **orchestration** service for managing containers at scale | Deploy and scale containers on managed Kubernetes |
| Azure Container Instances (ACI) | create a **single instance** container and start using it as you would a VM | Launch containers with hypervisor isolation |
| Azure Functions | serverless, code engine | Execute event-driven serverless code functions with an end-to-end development experience |
| Azure Logic Apps | serverless, workflow engine | Automate the access and use of data across clouds |
| Azure App Service | A Microsoft-managed application hosting service | Quickly create powerful cloud apps for web and mobile |

## Internet of Things
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure IoT Central | **Real-Time Message Ingestion**, Consume IoT services, SaaS, analyze data | Go from proof of concept to proof of value |
| Azure IoT Hub | Build your own IoT services, PaaS | Connect, monitor, and manage billions of IoT assets |
| Azure Sphere | Secure IoT services, security/telemetry data | Create, connect, and maintain secured intelligent IoT devices from the edge to the cloud |

## Management and governance
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Advisor | best practices recommendations | Your personalized Azure best practices recommendation engine |
| Azure Policy | consistent resource governance, Controls what can be done (regardless of the user), resource focused | Implement corporate governance and standards at scale |
| Azure Resource Manager templates | JSON, infrastructure-as-code, template | Deliver infrastructure as code for all your Azure resources using Resource Manager |
| Azure Blueprints | containers that made up of artifaces: Azure Services, Azure Policies, ARM Templates, RBAC, a set of resource group  | Enabling quick, repeatable creation of governed environments |
| Cloud Shell | browser based shell, accessed via azure portal | Streamline Azure administration with a browser-based shell |
| Microsoft Azure portal | graphical user interface, browser based | Build, manage, and monitor all Azure products in a single, unified console |
| Azure Monitor | logs, logs analytics, metrics | Full observability into your applications, infrastructure, and network |
| Azure Service Health | planned maintainence, service incidents | Personalized guidance and support for when issues in Azure services affect you |
| Azure Site Recovery | protects against complete region failure | Keep your business running with built-in disaster recovery service |
| Azure mobile app | manage azure resources via Android or iOS device | Stay connected to your Azure resources—anytime, anywhere |
| Microsoft Cost Management | **Cost Management + Billing** dashboard functionality in the Azure portal; billing: **invoices**, cost management: **cost analysis, set cost alerts, create budgets** | Monitor, allocate, and optimize cloud costs with transparency, accuracy, and efficiency |
| Microsoft Purview Compliance Manager | automatically assess and manage compliance across your multicloud environment. | Govern, protect, and manage your data estate |
| Az PowerShell module | install locally on Windows, macOS, and Linux | Azure PowerShell is a set of cmdlets for managing Azure resources directly from PowerShell |
| Azure Command-Line Interface (CLI) | cross-platform command-line **tool** | It allows the execution of commands through a terminal using interactive command-line prompts or a script |

## Migration
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Data Box | migrate data **physically** using disks and **shipping** it in a **box** | Appliances and solutions for data transfer to Azure and edge compute |
| Azure Migrate | Unified migration platform/hub, Assessment and migration tools, provide tools  | Simplify migration and modernization with a unified platform |

## Storage
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Files | PaaS, **SMB and NFS protocols**, Azure File shares, **azure file sync**  | Simple, secure and serverless enterprise-grade clouFdatad file shares |
| Archive Storage | Lowest-priced archive storage tier, data retrieval (**hydration**) costs, data is **offline**, requires **retrieval** | Industry leading price point for storing rarely accessed data |
| Storage Accounts | resources that need to be created to store your data objects: storage containers, file share, queues, tables  | Durable, highly available, and massively scalable cloud storage |
| Azure Disk Storage | IaaS, persistent disk for Azure VM | High-performance, highly durable block storage |
| Azure Data Lake Storage | Azure HDInsight, data lake analytics  | Scalable, secure data lake for high-performance analytics |
| Azure Storage Explorer | graphical interface to manage files and blobs | View and interact with Azure Storage resources |
| Queue Storage | service for storing large numbers of **messages** | Effectively scale apps according to traffic |
| Azure Blob Storage | **unstructured** data, **REST API**, image or video data, **backup** and **disaster recovery** | Massively scalable and secure object storage |

## Developer tool
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure DevTest Labs | an environment for automatically creating lab resources from pre-configured base items or ARM templates, all while utilizing the least administrative resources and effort | Quickly create environments using reusable templates and artifacts |
| Azure Repos | code repository | Get unlimited, cloud-hosted private Git repos for your project |
| Azure Boards | Track work with **Kanban boards**, backlogs, team dashboards, and custom reporting | Plan, track, and discuss work across your teams |

## Analytics
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Event Hubs | **real-time data ingestion service**, data pipelines, **millions of events** | Receive telemetry from millions of devices |
| Azure Synapse Analytics | insight across **data warehouses** and **big data systems**, **Apache Spark** for big data and **Data Explorer** for logs and metrics | Limitless analytics with unmatched time to insight |
| Azure Data Explorer | real-time analysis on large volumes of data streaming from applications, websites, IoT devices, **log and time series** analytics | Fast and highly scalable data exploration service |
| HDInsight | **open source**, **Batch Processing**, processing and analyzing big **data** | Provision cloud Hadoop, Spark, R Server, HBase, and Storm clusters |
| Azure Databricks | **Batch Processing** | Design **AI** with Apache Spark™-based analytics  |

## AI + machine learning
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Bot Services | A conversational AI service | Create bots and connect them across channels |
| Azure Cognitive Services | A pre-built AI service | Add cognitive capabilities to apps with APIs and AI services |
| Azure Machine Learning | A custom AI service | Use an enterprise-grade service for the end-to-end machine learning lifecycle |

