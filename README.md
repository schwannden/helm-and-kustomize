# Helm & Kustomization

This repository deploys a demo backend app in raw kubernetes object yaml files, using helm chart, and using kustomization. And discuss their differences. One can use this as a starting point to:

1. Learn helm chart.
2. Lean kustomization.
3. Learn the differences between them.

## Requirement

1. [k3d](https://github.com/k3d-io/k3d): we use this to provision a k8s cluster as playground.
2. [just](https://github.com/casey/just): our project command line interface (similar to `make` but much better).

## Preparation

1. `cd demo-backend`
2. `just build`

Our backend service has an api `/status`, and can be built in `demo-backend` folder with `just build`. The api detect `ENV`'s value and return different response accordingly.

* When `ENV` is `dev` or is missing, it returns
    - `{"status":"ok", "ENV":"dev", "cpu":0.4, "memory_usage":2243194880}`
* When `ENV` is not `dev`, it returns
    - `{"status":"ok","ENV":"actual env value"}`

## Case Study

### Raw K8s

1. Deploy with `just install`.
2. `curl 127.0.0.1:8080/status` to check for result.
3. Manually update the `deployment.yaml`'s `ENV` value.
4. Redeploy with `just install`.
5. `curl 127.0.0.1:8080/status` to check for result change.

Takeaways

1. Requires manually updating in a complicated yaml file.
2. Requires updating multiple location if we decide to change some shared value like port.
3. Not clear to our user which values are expose for customization.

### helm chart

1. Deploy with `just install`
2. `curl 127.0.0.1:8080/status` to check for result.
3. Manually update the `values.yaml`'s `ENV` value.
4. Upgrade helm installation with `just upgrade`.
5. `curl 127.0.0.1:8080/status` to check for result change.

Takeaways

1. Much more convenient to change common values through `values.yaml`.
2. Still has difficulty manage different deployment's specific settings.
    * Can't use different branch, as it is not friendly for continuous development.

### Kustomization

1. Deploy with `just install prod`
2. `curl 127.0.0.1:8080/status` to check for result.
3. `just uninstall prod`
4. `just install dev`
5. `curl 127.0.0.1:8080/status` to check for result change.

Takeaways

1. Much more convenient to maintain settings for different deployments.
2. lack the `helm` like installation management function (version control, rollback, ...etc).

### Helm + Kustomize

1. To be continued...