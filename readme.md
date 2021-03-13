<h1 align='center'> :snake: Classification and Regression </h1>

This content is taken from my studies using the book <a href='https://www.amazon.com/Artificial-Intelligence-Python-Comprehensive-Intelligent/dp/178646439X'>Artificial Intelligence with Python</a>

<h2 align='center'> Binarization </h2>

Is a process that transforms data into vectors of binary numbers, which makes classification algorithms more efficient.
<br>

***Example given by DeepAi about <a href='https://deepai.org/machine-learning-glossary-and-terms/binarization'>how Binarization is used</a>:***

_"In machine learning, even the most complex concepts can be transformed into binary form. For example, to binarize the sentence “The dog ate the cat,” every word is assigned an ID (for example dog-1, ate-2, the-3, cat-4). Then replace each word with the tag to provide a binary vector. In this case the vector: < 3,1,2,3,4 > can be refined by providing each word with four possible slots, then setting the slot to correspond with a specific word: < 0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1 >. This is commonly referred to as the bag-of-words-method."_
<br>


<h2 align='center'> Mean Removal </h2>

Remove a mean from every feature so that it could center on zero.

<br>
<h2 align='center'> Scaling </h2>

Using Min-Max Scaling you can normalize the range of independent data. In data processing, it is also known as data normalization and is generally performed during the data preprocessing step.
<br>

<h2 align='center'> Nomalization l1, l2 </h2>

_"We use the process of normalization to modify the values in the feature vector so that we
can measure them on a common scale. In machine learning, we use many different forms of
normalization. Some of the most common forms of normalization aim to modify the values
so that they sum up to 1 . L1 normalization, which refers to Least Absolute Deviations,
works by making sure that the sum of absolute values is 1 in each row. L2 normalization,
which refers to least squares, works by making sure that the sum of squares is 1."_