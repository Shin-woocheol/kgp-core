# kgp-core
This is the implementation of kgp-core algorithms, which is described in the following papaer:
- Unveiling Introverted Cohesive Structures in Hypergraphs: The (𝑘,𝑔,𝑝)-core computation

## How to use?

### there are two algorithm for kgp-core (NPA, ASAP)

- Input parameters
  - k
  - g
  - p
  - algorithm type
  - Path of the hypergraph data

example code
```
python main.py --k 5 --g 5 --p 0.8 --algorithm naive --network ./dataset/real/house_bills/network.hyp
python main.py --k 30 --g 30 --p 0.8 --algorithm ASAP --network ./dataset/real/house_bills/network.hyp
# output file with result will be stored in ./output/{algorithm}/{network_name}/{network_name}_{k}_{g}_{p}.txt
```

### other datasets
we only upload house_bills, gowalla, and kosarak datasets due to size limitation.
you can download other datasets from the following links:

Amazon : https://www.cs.cornell.edu/~arb/data/amazon-reviews/

Instacart : https://www.cs.cornell.edu/~arb/data/uchoice-Instacart/

Aminer : https://drive.google.com/file/d/12cvz-XtfQUbmj-gqlT9z4DKGMuhqLGjs/view - referenced from(https://github.com/toggled/vldbsubmission)


