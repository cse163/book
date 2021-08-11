# A Search Engine

In Take-home assessment 4, you will be implementing a search engine like Google to help find documents based on search queries. This slide will introduce you to some of the underlying ideas we will need to implement a search engine. We will see how all these pieces fit together to build a search engine in lecture and on your assignment!  
The goal of a search engine is to take a search query and return the set of the most relevant documents from a set of documents. The whole set of documents is generally called a **corpus** .  
##  Organizing with an Index  

To make our search engine fast, we will want to pre-process the documents so we can quickly answer the question  
> For a given word, what are all the documents that contain this word?
To do this, we construct a data structure called an **inverted index** to help answer this question. An inverted index is just a dictionary, where the keys are the words found in the corpus and the value for a key is a list of all the documents that have that word in them.  
For example, suppose our corpus had the three documents shown on the left of the picture below. The inverted index for this corpus is shown on the right in the image below. When processing the data, you will do some basic transformations to make everything lowercase and remove punctuation.  
```{image} https://static.us.edusercontent.com/files/2vV4eOC5105cnsjoxofM1v1j
:alt: TODO
:width: 408
:align: center
```

Notice the structure of the inverted index helps us answer this question. Want to find all the documents that mention "corgis"? Look up the key "corgis" and you can see Document 1 is the only one.  
When we want to handle **multi-word queries** (queries with more than one word), we will report all documents that contain at least one word from the query. For example, the query "corgis dogs" would return Document 1 and Document 3. Another way to think about this is the multi-word query is the result of unioning the results of all the single word queries (i.e., find all the documents that contain "corgies" and add on all the documents containing "dogs" [ignoring duplicates]).  
Part of your assignment will be writing the code to take a corpus and compute the inverted index from it. Another part of your assignment will be handling how to take a query and find all documents that match that query.  
