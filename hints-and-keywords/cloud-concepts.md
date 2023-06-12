# Cloud Concepts Keywords
| Concepts | Description | [Microsoft Cloud Computing Dictionary](https://azure.microsoft.com/en-ca/resources/cloud-computing-dictionary/) |
| --- | --- | --- |
| Scaling up/vertical scaling | capacity is increased within the resource, such as increasing processor or memory by resizing a virtual machine | Vertical scaling (scaling up) lets you increase or decrease computing power or databases as needed. |
| Scaling out/horizontal scaling | additional resource instances, such as adding other virtual machines or compute node/scale units | Horizontal scaling (scaling out) entails adding more databases or dividing a large database into smaller nodes, using a data partitioning approach called sharding |
| Elasticity | the ability to shape the resources needed automatically, burst and scale to meet any peak in demand, and return to a normal operating baseline | The ability to dynamically provision and de-provision computer processing, memory, and storage resources to meet changing demands without worrying about capacity planning and engineering for peak usage. [Learn more](https://azure.microsoft.com/en-ca/resources/cloud-computing-dictionary/what-is-elastic-computing/). | 
| Agility | deploying and configuring resources effectively and efficiently in a short space of time to meet any change in requirements or operational needs |  |
| High availability and geo-distribution | operate within the required or mandated Service Level Agreement (SLA) | ![sla-ha-diagram](https://learn.microsoft.com/en-us/azure/architecture/high-availability/images/high-availability-004.png) |
| Disaster recovery | set of initiatives designed to ensure that critical business systems will be protected, despite serious incidents, and recovered to an operational state within a defined period; this is achieved by failing over to systems that have been replicated in another region |  |
| Scalability | ability of a system to handle increased loads while still meeting availability goals |  |

## Comparison
| Concepts | Description |
| --- | --- |
| High availability | When systems fail and are not available, you can run a second instance in the same Azure region |
| Disaster recovery | When systems fail and are not available, you can run a second instance in another Azure region |
| Backup | When data is corrupted, deleted, lost, or irretrievable (ransomware), you can restore the instance from another copy of the system |

## Availability Component
| Concepts | Description | Figure |
| --- | --- | --- |
| [Availability Sets](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview) | Protection within a data centre | ![availability-set-image](https://learn.microsoft.com/en-us/azure/virtual-machines/media/virtual-machines-common-manage-availability/md-fd-updated.png) |
| [Availability Zones](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview) | Protection within a region; one or more data centres | ![availability-zone-image](https://learn.microsoft.com/en-us/azure/reliability/media/availability-zones.png) |
| [Region Pairs](https://learn.microsoft.com/en-us/azure/reliability/cross-region-replication-azure) | protection across a region; pairs are located 300 miles or more apart where possible | ![region-pair-image](https://learn.microsoft.com/en-us/azure/reliability/media/cross-region-replication.png) |
| VM scale sets | IaaS resource service with built-in autoscaling features for VM-based workloads, identical VMs can be created through VM scale sets, which provides the automatic scaling functionality expected from a cloud model |  |

# Types of Clouds
| Type | Description | Analogy |
| --- | --- | --- |
| Public cloud | a *shared entity (multi-tenant)* computing model. Hardware and resources such as compute, storage, and networking are owned by the cloud provider and shared with other tenants on the platform | *an apartment block*, where you are a tenant that shares the building with other tenants; you pay rent to a landlord for your apartment |
| Private cloud | a *dedicated entity (single-tenant)* computing model. Hardware and resources such as compute, storage, and networking are dedicated to your organization use only | a house as opposed to an apartment block; you are the single tenant, and you do not share the building with any other tenants. You either own the building or you rent the property and pay a landlord |
| Hybrid cloud | a combination of a *shared entity (multi-tenant)* computing model and a *dedicated entity (single-tenant)* computing model | Some computing resources you choose to have running in your private cloud environment and some resources you choose to have running in a public cloud environment based on your needs |
| Azure Dedicated Host |  provides physical virtualization hosts dedicated to individual customers to host their Azure VMs for Windows and Linux workloads | this means that the building and its contents are yours and that you are not sharing with anybody else. This is not a hotel room—this is a house, a single-tenancy occupied building—and each room (or VM) is yours |