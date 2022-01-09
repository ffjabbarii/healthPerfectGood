# K8s probe demo

This is a demo to confirm the function of Readiness Probe and Liveness Probe in K8s. The demo is intended to help deepen your understanding of the Probe.
The web application part was coded in flask. These probe uses an HTTP GET request.

*reference*  

kubernates documentation "Configure Liveness, Readiness and Startup Probes" https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/

# DEMO

When you run it, you will see the change in the pod as shown below.

```bash

$ kubectl get po
NAME        READY   STATUS    RESTARTS   AGE
hc-webapp   0/1     Running   0          18s

$ kubectl get po
NAME        READY   STATUS    RESTARTS   AGE
hc-webapp   1/1     Running   0          68s

$ kubectl get po
NAME        READY   STATUS    RESTARTS   AGE
hc-webapp   0/1     Running   1          75s

```
 
# Environment
 
python 3.9.2 (no need)

# Author
 
* kodacme
* Software engineer
* kodac.saito@kodac.me
