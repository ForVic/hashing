# Open Addressing vs. Closed Addressing
Until recently I was unaware that there were two different implementations of hash tables, when it came to hash collisions. Last year, during an interview where I was asked to implement what amounted to a hash table, I was hinted to and derived the closed addressing version of a hash table. Since then I (naively) ran with the assumption that that was the way in which all hash tables were implemented, considering the only time I had actually researched it was with regards to Java's HashMap, which was is implemented using closed adressing in [OpenJDK Java] (https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/HashMap.java#L617). This is just my basic implementation of both, to help in increasing my understanding, as well as my a quick summary of what I gathered from reading about the two implementations. I will implement the closed addressing version using a linked list. We will implement the naive version of open addressing using linear probing. Can read about some various probing techniques [here](https://programming.guide/hash-tables-open-addressing.html).

## Open Addressing
- Python uses open addressing (I didn't actually know this)
    - No need for complex data structures for buckets since only a single element is in each bucket at a time.
    - C struct in python implementation is \<hash, key, value\>, as a C struct.
    - [details here 296-297](https://hg.python.org/cpython/file/52f68c95e025/Objects/dictobject.c)
- You don't have to allocate new nodes when keys are inserted.
- Less memory overhead, since you aren't having to maintain a separate structure.
- Is forced to use tombstones in removal (aka mark as deleted instead of actually delete).

## Closed Addressing
- Used in OpenJDK Java.
    - They use trees as the storage method of choice for the 'bins'.
- Often implemented with LinkedLists, Vectors, and Trees.
- No maximum load factor (aka a ton of hash collisions makes it worse and worse forever).
- Since we have to use a linked list here, likely we are doing some sort of dynamic heap allocation that removes some of the data locality benefits of using an underlying array as the storage method.

