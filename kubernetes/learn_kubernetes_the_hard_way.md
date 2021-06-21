**Learn Kubernetes the Hard Way** 
*AWS edition*
https://github.com/prabhatsharma/kubernetes-the-hard-way-aws
---

- Prerequesites
    - AWS CLI installed
    - aws configure set default.region us-west-2
- Installing the Client Tools
    - cfssl and cfssljson to provision a PKI (public key infrastructure) and generate TLS certs
    - all these commands are for osx or linux, so gotta do this in an ec2 instance
    - kubeCTL to interact with kubernetes API server
- provisioning Compute resources
    - K8s assumes a flat network which lets containers and nodes communicate
    - create a VPC:
        - ubuntu needs update before installing awscli