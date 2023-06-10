# Cloud Concepts Keywords
| Concepts | Description |
| --- | --- |
| Scaling up/vertical scaling | capacity is increased within the resource, such as increasing processor or memory by resizing a virtual machine |
| Scaling out/horizontal scaling | additional resource instances, such as adding other virtual machines or compute node/scale units |
| Elasticity | the ability to shape the resources needed automatically, burst and scale to meet any peak in demand, and return to a normal operating baseline |
| Agility | deploying and configuring resources effectively and efficiently in a short space of time to meet any change in requirements or operational needs |
| High availability and geo-distribution | operate within the required or mandated Service Level Agreement (SLA) |
| Disaster recovery | set of initiatives designed to ensure that critical business systems will be protected, despite serious incidents, and recovered to an operational state within a defined period; this is achieved by failing over to systems that have been replicated in another region |
| Scalability | ability of a system to handle increased loads while still meeting availability goals |

## Comparison
| Concepts | Description |
| --- | --- |
| High availability | When systems fail and are not available, you can run a second instance in the same Azure region |
| Disaster recovery | When systems fail and are not available, you can run a second instance in another Azure region |
| Backup | When data is corrupted, deleted, lost, or irretrievable (ransomware), you can restore the instance from another copy of the system |

## Availability Component
| Concepts | Description |
| --- | --- |
| Availability Sets | Protection within a data center |
| Availability Zones | Protection within a region |
| Region Pairs | protection across a region | 
| VM scale sets | IaaS resource service with built-in autoscaling features for VM-based workloads, dentical VMs can be created through VM scale sets, which provides the automatic scaling functionality expected from a cloud model |