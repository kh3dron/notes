### https://kubernetes.io/docs/tutorials/hello-minikube/

- Install minicube via exe
- minikube start
- kubectl get po -A: lists services
- minikube dashboard: a pretty web interface
- kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.4
- kubectl expose deployment hello-minikube --type=NodePort --port=8080
- kubectl get services hello-minikube

### https://kubernetes.io/docs/tutorials/kubernetes-basics/

- 1 - Create a Kubernetes Cluster
    - Kubernetes coordinates a highly available cluster of computers that are connected to work as a single unit
    - Two parts to a k8s cluster: the Control Plane and Nodes
        - Nodes can be VMs or physical hosts
        - Each node has a cubelet, an agent for managing the node and communicating with the plane
        - Nodes also have container management software, like containerd or Docker
        - clusters handling production envs should have at least 3 nodes
    - Minicube deploys a simple cluster with one node. Tutorial:
        - minikube start
        - minikube version
        - kubectl version
        - kubectl cluster-info: shows IPs of control plane, DNS
        - kubectl get-nodes: shows status of nodes
- 2 - Use kubectl to Create a Deployment
    - With a running cluster, you can deploy containerized applications on it by creating a Kubernets Deplopyment Configuration
    - Once instances are created, the Kubernetes Deployment Controller monitors the instances for self-healing
    - Pre-orchestration, installation scripts would start apps, but would struggle to recover from machine failure
    - kubectl: CLI wrapper for Kubernetes API
    - Commands tend to be formatted as: kubectl <action> <resource>
    - Deploying an app:
        - kubectl get nodes
        - kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
            - this did a few things: first, searched for a node to run on
            - scheduled the application to run on the node
            - configured the cluster to reschedule the instance on a new node if needed 
        - kubectl get deployments
        - You can access the pod through a proxy
- 3 - Viewing Pods and Nodes
    - A pod stores some containers and some shared resources:
        - Shared storage as volumes
        - Shared networking as a cluster IP address
        - Container image versions or ports to use
    - A pod is effectively a logical host - containers within a pod are tightly coupled
    - Some commands:
        - kubectl get
            - kubectl get pods
        - kubectl describe
            - kubectl describe pods
        - kubectl logs
        - kubectl exec
    