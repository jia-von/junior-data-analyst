# Exam AZ-900: Microsoft Azure Fundamentals Hints and Keywords
I have finally passed my Exam AZ-900: Microsoft Azure Fundamentals with a score of 865 on June 2023. Here are some of things that helped me remember and understand AZ-900.

## Describe cloud concepts
### Describe cloud service types
| Service | Keywords | Products |
| --- | --- | --- |
| Infrastructure as a Service (IaaS) | **complete control of**: hardware, virtual machine (VM), networking | Azure VMs, Azure Disk Storage, Azure Virtual Networks (VNet) |
| Platform as a Service (PaaS) | provides ready-to-use environment, usually azure product with fancy names | Azure App Service, Azure SQL Database, Cosmos DB, Azure Files, Azure Active Directory Domain Services |
| PaaS Serverless | serverless, business logic priority | Azure Functions, Azure Logic App |

## Azure Product Service
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Logic Apps | serverless, workflow engine | Automate the access and use of data across clouds |
| Azure Functions | serverless, code engine | Execute event-driven serverless code functions with an end-to-end development experience |
| Azure ExpressRoute | traffic does not route (traverse) the internet | Experience a fast, reliable, and **private** connection to Azure |
| VPN Gateway | encrypted traffic, point-to-site, site-to-site | Establish secure, cross-premises connectivity |
| Azure Active Directory (Azure AD) | providing authentication and authorization for users, MFA, conditional access, SSO | Synchronize on-premises directories and enable single sign-on |
| Microsoft Defender for Cloud | provides security policy, compliance manager, sercure score, security alerts, just-in-time (JIT) network access | Protect your multi-cloud and hybrid environments |
| Content Delivery Network | deliver videos and streaming | Fast, reliable content delivery network with global reach |
| Azure Service Health | planned maintainence, service incidents | Personalized guidance and support for when issues in Azure services affect you |
| Azure Policy | consistent resource governance, Controls what can be done (regardless of the user), resource focused | Implement corporate governance and standards at scale |
| Azure Arc |  simplifies governance and management by delivering a consistent multicloud and on-premises management platform | Secure, develop, and operate infrastructure, apps, and Azure services anywhere |

## Databases
| Product Name | Keywords | One-liner |
| --- | --- | --- |

## Security
| Product Name | Keywords | One-liner |
| --- | --- | --- |
| Azure Information Protection | encrypt documents and emails | Better protect your sensitive information—anytime, anywhere |
| Azure DDoS Protection | threats and attacks, network layer (OSI), perimeter layer (DiD) | Protect your Azure resources from distributed denial-of-service (DDoS) attacks |
| Microsoft Sentinel | **sentinel** definition: a soldier or guard whose job is to sant and keep watch, SIEM, SOAR, AI based security, response to threats just like a guard | Cloud-native SIEM and intelligent security analytics |  
| Azure Firewall | applied at **VNet level**, control traffic flow, network address translation (NAT), **filter** traffic across many VNets | Protect your Azure Virtual Network resources with cloud-native network security |
| Network Security Group (NSG) | allow or deny, connect using port, inbound/outbound rules, associated with VM **network interface controller (NIC)** and a **subnet** but not a VNet |  |
| Azure Key Vault | vault = to safekeep, secrets, keys | Safeguard and maintain control of keys and other secrets |