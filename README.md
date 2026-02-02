<h1 align="center">Krish Singh</h1>
<p align="center">
  <small>
    Systems · Backend · Containers · Retrieval Systems
  </small>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=krishsingh16&style=flat-square&color=6aa84f" />
</p>

---

<img src="https://user-images.githubusercontent.com/74038190/212897744-8c0b2f4c-38f6-4b2b-bc1f-4a9e5f7c9b7a.gif" height="2" width="100%"/>

## About

<img align="right" src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" width="90"/>

I’m a backend and systems-leaning engineer who enjoys building things **close to the metal** and then questioning whether the abstractions were worth it.

Most of my work lives at the intersection of:
- distributed systems  
- containers & Linux internals  
- retrieval-augmented generation (RAG)  
- Java done *properly*, not ceremonially  

I tend to learn by breaking things, reading source code, and rebuilding them until the mental model sticks.

---

<img src="https://user-images.githubusercontent.com/74038190/212897744-8c0b2f4c-38f6-4b2b-bc1f-4a9e5f7c9b7a.gif" height="2" width="100%"/>

## Current Focus — ContextQA

<img align="right" src="https://cdn-useast1.kapwing.com/static/templates/confused-math-lady-meme-maker-TVtw6-LM49LSMFgm-full.jpg" width="120"/>

A hybrid **RAG system** designed to make LLM outputs *traceable*, not magical.

The core idea is a **plant metaphor** to visualize data lineage:
documents → chunks → embeddings → answers.

Not because it’s cute — because most RAG systems are black boxes, and debugging hallucinations without observability is pointless.

**Highlights**
- Vector search for recall  
- Document graphs for precision  
- Explicit lineage from source → answer  

**Stack**
- Java (Spring Boot)
- PostgreSQL + pgvector
- React

Status: *actively growing* 🌱  
If it dies, I’ll know exactly **why**.

---

<img src="https://user-images.githubusercontent.com/74038190/212897744-8c0b2f4c-38f6-4b2b-bc1f-4a9e5f7c9b7a.gif" height="2" width="100%"/>

## Recently Built — J-Container

<img align="right" src="https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif" width="120"/>

A **rootless container runtime** built from scratch in **C + Java**.

This started as a learning exercise and ended up being faster than I expected.

| Metric | J-Container | Docker |
|------|-----------|--------|
| Startup Time | **~138 ms** | ~750 ms |
| Architecture | Java + native C | Go (client/daemon) |

Why it’s fast:
- minimal OCI overhead  
- direct use of Linux namespaces  
- fewer abstractions between intent and syscall  

This wasn’t about “beating Docker”.  
It was about understanding **why containers work at all**.

---

<img src="https://user-images.githubusercontent.com/74038190/212897744-8c0b2f4c-38f6-4b2b-bc1f-4a9e5f7c9b7a.gif" height="2" width="100%"/>

## Work Status

<img align="right" src="https://a.pinatafarm.com/620x500/41dca8f897/spongebob-waiting.jpg" width="120"/>

Currently independent.

Which means:
- open-source contributions  
- deep personal projects  
- building things I’d actually want to maintain in production  

I’m open to backend / systems roles where:
- correctness matters  
- abstractions are questioned  
- “because the framework says so” is not an argument  

---

<img src="https://user-images.githubusercontent.com/74038190/212897744-8c0b2f4c-38f6-4b2b-bc1f-4a9e5f7c9b7a.gif" height="2" width="100%"/>

## Education

<img align="right" src="https://media.giphy.com/media/l0HlRnAWXxn0MhKLK/giphy.gif" width="120"/>

**M.Sc. Computer Science**  
Osmania University (2022–2024)

Formal education gave me structure.  
Most of the real learning came from:
- kernel panics  
- broken builds  
- reading code that was never meant to be read  

---

<img src="https://user-images.githubusercontent.com/74038190/212897744-8c0b2f4c-38f6-4b2b-bc1f-4a9e5f7c9b7a.gif" height="2" width="100%"/>

## Tools I Actually Use

<p align="left">
  <img src="https://skillicons.dev/icons?i=java,c,spring,postgres,linux,docker,git,vim,python,react&perline=8"/>
</p>

- **Languages:** Java, C, Python  
- **Backend:** Spring Boot, Hibernate, REST  
- **Systems:** Linux internals, containers, GCC  
- **Editor:** Vim (voluntarily)

---

<img src="https://user-images.githubusercontent.com/74038190/212897744-8c0b2f4c-38f6-4b2b-bc1f-4a9e5f7c9b7a.gif" height="2" width="100%"/>

## Philosophy

```java
while (curiosity > comfort) {
    breakThings();
    understandWhy();
    rebuild(cleaner);
}
```
Abstractions are useful.
Understanding what they hide is mandatory.

<p align="center"> <small> Portfolio: https://krishsingh16-portfolio.vercel.app <br/> If you’re hiring and this resonates, we’ll probably get along. </small> </p>
