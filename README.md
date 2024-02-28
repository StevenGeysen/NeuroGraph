# NeuroGraph
Graph to summarise brain regions and their functions

## Example
```mermaid
classDiagram
    dACC <-- LC
    dACC <|-- dmPFC
    class vmPFC["Ventral medial prefrontal cortex"]{
        pathway(DA)
        functions(subjective values)
        subgraph()
        sources()
    }
    
    class dmPFC["Dorsal medial prefrontal cortex"]{
        pathway(DA)
    }
    
    class dACC["Dorsal anterior cingulate cortex"]{
        pathway(DA)
        functions()
        subgraph(dmPFC)
        
    }
    
    class LC["Locus coeruleus"]{
        pathway(DA)
        functions()
        subgraph()
        sources()
    }
```

---

# References
* [Mermaid diagram](https://mermaid.js.org/syntax/classDiagram.html)
* [Silvetti et al. (2018)](https://dx.plos.org/10.1371/journal.pcbi.1006370)
* [Yao et al. (2023)](https://doi.org/10.1016/j.neuroimage.2023.120326)
