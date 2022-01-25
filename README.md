# EXTRA (EXplanaTion RAnking) Datasets

## Papers
- Lei Li, Yongfeng Zhang, Li Chen. [EXTRA: Explanation Ranking Datasets for Explainable Recommendation](https://lileipisces.github.io/files/SIGIR21-EXTRA-paper.pdf). SIGIR'21 Resource.
- Lei Li, Yongfeng Zhang, Li Chen. [On the Relationship between Explanation and Recommendation: Learning to Rank Explanations for Improved Performance](https://arxiv.org/abs/2102.00627). 2021.

## Datasets to [download](https://drive.google.com/drive/folders/1Kb4pOCUja1EgDlhP-YQI8AxofHBkioT5?usp=sharing)
- Amazon Movies & TV
- TripAdvisor Hong Kong
- Yelp 2019

If you are interested in how to build models on the datasets, please refer to [BPER](https://github.com/lileipisces/BPER).

## Data format
- **IDs.pickle** can be loaded via the pickle package as a python list, where each record is a python dict in the form of
```
{'user': '7B555091EC0818119062CF726B9EF5FF',  # str
'item': '1068719',  # str
'rating': 5,  # int, not important to the ranking task
'time': '2017-05-06', # str in the format of YYYY-MM-DD, not available on TripAdvisor
'exp_idx': ['34', '85'],  # a list of str, they are the indices of explanations after sentence grouping via LSH
'oexp_idx': ['91', '15']}  # a list of str, they are the indices of original sentences, corresponding to senID in the following
```
- Open **id2exp.json** via a text editor, e.g., Sublime, if you are curious about what the explanation indices correspond to. Or you can load it via [testing.py](testing.py) by updating the parameters (line 5-7).
---
- **IDs.txt** and **id2exp.txt** are compatible with **IDs.pickle** and **id2exp.json**. It would be easier to check the content with plain text files.
- Each line in **IDs.txt** is in the format of ```userID::itemID::rating::timestamp::expID:expID::senID:senID```, where timestamp is not available on TripAdvisor, and expID/senID are separated by ":" when there are multiple explanations.
- Each line in **id2exp.txt** is in the format of ```expID::explanation sentence```.
- You can load the two files via [movielens_load.py](movielens_load.py) by updating the paths (line 1-2).
---
- **Folders** named 1, 2, 3, 4 and 5 are data splits.
- Each folder contains **train.index** and **test.index** which indicate the indices of their records in the list of IDs.pickle/IDs.txt.
- **train.index**/**test.index** contain a line of numbers (indices), e.g., 5 8 9 10.

## Creation steps
- Run the scripts in the following order:
- Modify [format_amazon.py](format_amazon.py), including the path (line 6, 7), the keys (line 13, 14, 17, 19-23), and how you load and iterate over each review (line 10) if your data are stored in other data formats, such as JSON, Excel or TXT. Remove line 13-16, if your dataset has no summary or tip, which is meant to include as much textual data as possible. **This script is not limited to Amazon datasets. You can modify it to apply to other datasets**.
- Update the paths (line 6, 7) in [process_sentence.py](process_sentence.py).
- Update the parameters (line 6-10) in [group_sentence.py](group_sentence.py).
- Update the paths (line 5-9) in [keep_valid.py](keep_valid.py).
- Update the paths (line 6-9) in [movielens.py](movielens.py), if you want to process the data into the MovieLens format.

## Friendly reminder
- Run the program on a machine with sufficient memory
- Creating the datasets may take some time (e.g., hours for Yelp)

## Code dependencies
- Python 3.6
- NLTK
- [Datasketch](http://ekzhu.com/datasketch/lsh.html)

## Citations
```
@inproceedings{SIGIR21-EXTRA,
	title={EXTRA: Explanation Ranking Datasets for Explainable Recommendation},
	author={Li, Lei and Zhang, Yongfeng and Chen, Li},
	booktitle={SIGIR},
	year={2021}
}
@article{2021-BPER,
	title={On the Relationship between Explanation and Recommendation: Learning to Rank Explanations for Improved Performance},
	author={Li, Lei and Zhang, Yongfeng and Chen, Li},
	journal={arXiv preprint arXiv:2102.00627},
	year={2021}
}
```
