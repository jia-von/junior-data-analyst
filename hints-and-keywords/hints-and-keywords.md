# Exam AZ-900: Microsoft Azure Fundamentals Hints and Keywords
I have finally passed my Exam AZ-900: Microsoft Azure Fundamentals with a score of 865 on June 2023. Here are some of things that helped me remember and understand AZ-900.

## Describe cloud concepts
### Describe cloud service types
| Service | Keywords | Products |
| --- | --- | --- |
| Infrastructure as a Service (IaaS) | **complete control of**: hardware, virtual machine (VM), networking | Azure VMs, Azure Disk Storage, Azure Virtual Networks (VNet) |
| Platform as a Service (PaaS) | provides ready-to-use environment, usually azure product with fancy names | Azure App Service, Azure SQL Database, Cosmos DB, Azure Files, Azure Active Directory Domain Services |
| PaaS Serverless | serverless, business logic priority | Azure Functions, Azure Logic App |

## Networking
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure ExpressRoute | traffic does not route (traverse) the internet | Experience a fast, reliable, and **private** connection to Azure |
| VPN Gateway | encrypted traffic, point-to-site, site-to-site | Establish secure, cross-premises connectivity |
| Content Delivery Network | deliver videos and streaming | Fast, reliable content delivery network with global reach |
| Azure Arc |  simplifies governance and management by delivering a consistent multicloud and on-premises management platform | Secure, develop, and operate infrastructure, apps, and Azure services anywhere |

## Databases

## Security
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Information Protection | encrypt documents and emails | Better protect your sensitive information—anytime, anywhere |
| Azure DDoS Protection | threats and attacks, network layer (OSI), perimeter layer (DiD) | Protect your Azure resources from distributed denial-of-service (DDoS) attacks |
| Microsoft Sentinel | **sentinel** definition: a soldier or guard whose job is to sant and keep watch, SIEM, SOAR, AI based security, response to threats just like a guard | Cloud-native SIEM and intelligent security analytics |  
| Azure Firewall | applied at **VNet level**, control traffic flow, network address translation (NAT), **filter** traffic across many VNets | Protect your Azure Virtual Network resources with cloud-native network security |
| Network Security Group (NSG) | allow or deny, connect using port, inbound/outbound rules, associated with VM **network interface controller (NIC)** and a **subnet** but not a VNet |  |
| Azure Key Vault | vault = to safekeep, secrets, keys | Safeguard and maintain control of keys and other secrets |
| Azure Active Directory (Azure AD) | providing authentication and authorization for users, MFA, conditional access, SSO | Synchronize on-premises directories and enable single sign-on |
| Microsoft Defender for Cloud | provides security policy, compliance manager, sercure score, security alerts, just-in-time (JIT) network access | Protect your multi-cloud and hybrid environments |
| Azure Front Door | application delivery network (ADN) service, operates at the geographic layer and is not regional | Modern cloud CDN that delivers optimized experiences to your users anywhere |

## Containers
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Kubernetes Service (AKS) | orchestration service for managing containers at scale | Deploy and scale containers on managed Kubernetes |
| Azure Container Instances (ACI) | create a single instance container and start using it as you would a VM | Launch containers with hypervisor isolation |
| Azure Functions | serverless, code engine | Execute event-driven serverless code functions with an end-to-end development experience |
| Azure Logic Apps | serverless, workflow engine | Automate the access and use of data across clouds |
| Azure App Service | A Microsoft-managed application hosting service | Quickly create powerful cloud apps for web and mobile |

## Internet of Things
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure IoT Central | Consume IoT services, SaaS, analyze data | Go from proof of concept to proof of value |
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

## Migration
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Data Box | migrate data **physically** using disks and **shipping** it | Appliances and solutions for data transfer to Azure and edge compute |

## Storage
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Files | PaaS,  | Simple, secure and serverless enterprise-grade cloud file shares, **SMB and NFS protocols**, Azure File shares |
| Archive Storage | Lowest-priced archive storage tier, data retrieval (**hydration**) costs, data is **offline**, requires **retrieval** | Industry leading price point for storing rarely accessed data |
| Storage Accounts | resources that need to be created to store your data objects: storage containers, file share, queues, tables  | Durable, highly available, and massively scalable cloud storage |
| Azure Disk Storage | IaaS, persistent disk for Azure VM | High-performance, highly durable block storage |
| Azure Data Lake Storage | Azure HDInsight, data lake analytics  | Scalable, secure data lake for high-performance analytics |

## Developer tool
