**Learn Kubernetes the Hard Way** 
*AWS edition*
https://github.com/prabhatsharma/kubernetes-the-hard-way-aws
---

- Prerequesites
    - AWS CLI installed
    - aws configure set default.region us-west-2
- Installing the Client Tools
    - cfssl and cfssljson to provision a PKI (public key infrastructure) and generate TLS certs
    - kubeCTL to interact with kubernetes API server
- Provisioning Compute resources
    - K8s assumes a flat network which lets containers and nodes communicate
    - create a VPC:
        - get aws cli sonfigured right on mac: download sec creds from root aws account - NOT through iam   
        - enable DNS inside the VPC
    - Create a subnet for the cluster - large enough for all the nodess ofc
    - Create an internet gateway, name it kubernetees, and attach it to VPC
    - Create a route table, tag it, associate to VPC, outbound traffic allowed to whole internet CIDR
    - Load Balancer
        - some of these commands are defining bash variables that point to ARNs, as the results of queries running in AWS EC2 CLI commands. The ARN vars are used later
    - ELBs as the Kubernetes public adress
    - Create an SSH key rq
    - Launching controllers and workers
        - use a bash loop to spawn some t2.micros
- Provisioning a Certficate Authority & TLS Certificates
    - Generate the CA config file, cert, priv key as ca-key.pem and ca.pem
    - generate client and server certs for each k8s component, client cert for k8s admin user as admin-key.pem and admin.pem 
    - Node authorizer: allows kubelets to perform API operations. Generate a cert and priv key for each worker node
    - Controller manager client cert
    - Generate the kube-proxy client certificate and private key
    - Scheduler cliient certificate and private key
    - Kubernetes API server certificate
    - Service account key pair
    - The kube-proxy, kube-controller-manager, kube-scheudler, and kubelet client certs are used to generate client auth config files
- Generating Kubernetes Configuration Files for Authentication
    