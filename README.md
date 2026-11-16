<p align="center">
  <img src="assets/banner.svg" width="100%" alt="Matan Weisz: DevOps engineer, cloud and AI infrastructure" />
</p>

<p align="center">
  <a href="https://linkedin.com/in/matanweisz"><img src="https://img.shields.io/badge/LinkedIn-say_hi-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <img src="https://img.shields.io/badge/based_in-Herzliya,_Israel-1f8f84?style=flat-square" alt="Based in Herzliya, Israel" />
  <img src="https://img.shields.io/badge/status-open_to_new_roles-2ea44f?style=flat-square" alt="Open to new roles" />
</p>

I'm a DevOps engineer. I like infrastructure that does its job so well nobody has to think about it, and most of mine lives in Kubernetes, Terraform and CI/CD on AWS and GCP. What excites me most is the infrastructure behind AI: getting models served fast on GPUs, and giving teams a safe, affordable way to build with LLMs.

```yaml
apiVersion: v1
kind: Engineer
metadata:
  name: matan-weisz
  location: herzliya-israel
spec:
  craft: [kubernetes, terraform, gitops, aws, gcp]
  goingDeepOn: [llm-inference, gpu-platforms, ai-gateways, ai-agents]
  believesIn:
    - automate the boring parts first
    - if it can't be rebuilt from code, it isn't done
    - small changes, shipped often, easy to roll back
```

## What I work on

<table>
  <tr>
    <td width="50%" valign="top">
      <b>Platforms on Kubernetes</b><br/>
      Clusters that teams can trust, with sensible defaults and upgrades nobody dreads.
    </td>
    <td width="50%" valign="top">
      <b>Everything as code</b><br/>
      Terraform for the cloud, Git as the source of truth, and Argo CD keeping the two in sync. If an environment disappears, it comes back from a commit.
    </td>
  </tr>
  <tr>
    <td valign="top">
      <b>AI infrastructure</b><br/>
      How open models get served efficiently on GPUs, and how one gateway can keep every team's LLM keys, limits and costs in one place.
    </td>
    <td valign="top">
      <b>AI in the delivery loop</b><br/>
      Agents that use real tools through MCP, and AI that reads a failed pipeline and points at the cause. A coding assistant is part of my daily workflow.
    </td>
  </tr>
</table>

## Skill tree

<table>
  <tr>
    <td width="170"><b>Core</b><br/><sub>my day to day</sub></td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: light)" srcset="https://skillicons.dev/icons?i=kubernetes%2Cdocker%2Cterraform%2Caws%2Cgcp%2Cgithubactions%2Cgitlab%2Clinux%2Cbash%2Cpy%2Cgit&theme=light" />
        <img src="https://skillicons.dev/icons?i=kubernetes,docker,terraform,aws,gcp,githubactions,gitlab,linux,bash,py,git&theme=dark" height="40" alt="Kubernetes, Docker, Terraform, AWS, GCP, GitHub Actions, GitLab, Linux, Bash, Python, Git" />
      </picture>
      <br/><sub>Helm · Argo CD · Crossplane · Jenkins · Prometheus · Grafana</sub>
    </td>
  </tr>
  <tr>
    <td><b>AI infrastructure</b><br/><sub>where I'm going deepest</sub></td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: light)" srcset="https://skillicons.dev/icons?i=go%2Cfastapi&theme=light" />
        <img src="https://skillicons.dev/icons?i=go,fastapi&theme=dark" height="40" alt="Go, FastAPI" />
      </picture>
      <br/><sub>vLLM · SGLang · GPUs on Kubernetes · LLM gateways · MCP · Claude Code · LLM APIs · n8n</sub>
    </td>
  </tr>
  <tr>
    <td><b>App stack</b><br/><sub>for the tools I build</sub></td>
    <td>
      <picture>
        <source media="(prefers-color-scheme: light)" srcset="https://skillicons.dev/icons?i=react%2Cts%2Cvite%2Ctailwind%2Csupabase&theme=light" />
        <img src="https://skillicons.dev/icons?i=react,ts,vite,tailwind,supabase&theme=dark" height="40" alt="React, TypeScript, Vite, Tailwind, Supabase" />
      </picture>
    </td>
  </tr>
</table>

## Project shelf

<!-- Newest and best first. Each card: name, one line on why it's interesting, the stack. -->
<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/matanweisz/claude-devops-interviews"><b>claude-devops-interviews</b></a><br/>
      An AI interviewer built on Claude Code. It runs realistic DevOps interviews, adjusts to your level and remembers your weak spots between sessions.<br/>
      <sub><code>Claude Code</code> <code>LLM agents</code> <code>DevOps</code></sub>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/matanweisz/bigarch-devops-assignment"><b>bigarch-devops-assignment</b></a><br/>
      An HPC scheduler wired into cloud-native monitoring. Slurm is built from source and installed by SaltStack, and its jobs report live load to Prometheus and Grafana on K3s. One <code>vagrant up</code> builds the whole thing.<br/>
      <sub><code>Slurm</code> <code>K3s</code> <code>SaltStack</code> <code>Prometheus</code></sub>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <a href="https://github.com/matanweisz/package-tracker-api"><b>package-tracker-api</b></a><br/>
      An event-driven package tracking API where reads and writes take separate paths (CQRS).<br/>
      <sub><code>Python</code> <code>Kafka</code> <code>MongoDB</code> <code>Redis</code></sub>
    </td>
    <td valign="top">
      <a href="https://github.com/matanweisz/deploy-n8n-production"><b>deploy-n8n-production</b></a><br/>
      One script turns a clean VM into a production n8n, with PostgreSQL behind an nginx reverse proxy.<br/>
      <sub><code>Bash</code> <code>Docker Compose</code> <code>PostgreSQL</code> <code>nginx</code></sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Always happy to talk infrastructure, AI or a good postmortem. <a href="https://linkedin.com/in/matanweisz">Find me on LinkedIn</a>.</sub></p>
