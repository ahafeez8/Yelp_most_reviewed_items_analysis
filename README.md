# Yelp_most_reviewed_items_analysis
We use Yelp dataset challenge 2018's release of dataset: https://www.yelp.co.uk/dataset
This project outputs a suggestion for businesses about their most reviewed positively and negatively reviwed items. 
It takes on assumptions:
- Customers will always mention what they liked or disliked the most about that business. 
- The image-review mapping was assumed on the basis of similarity of words or phrases of photo captions and review text. 
- Rating given on a review represent sentiment attached to both the textual review and photo(s) attached to it

## Steps:
Since no direct link between reviews and attached images exist, we approximate that by the approach used in 'Combining Image and Language to Predict and Understand the Usefulness of Yelp Reviews' by David Z Liu. 
Load data into image_review_pairing.py and it outputs related pairs and rating into photo_rev_pairs.json file. 

Then we seperate out images from main dataset. Place the get_pics.py and photo_rev_pairs.json into the image dataset folder and it'll seperate out required images. 

Then perform object recognition using our trained model on AlexNet. Use test.py to train.
### Note: 
-Add bvlc_alexnet.npy into the object recognition folder. Get bvlc_alexnet.npy zippped here: https://drive.google.com/file/d/1hUB_w31W629n7Mqhi9iGtjSQUNSAA8hk/view?usp=sharing
- Place data.tar into objectrecognition/models/ and get it from here: https://drive.google.com/file/d/1J4TXiIAQcWj8xljtaLlgGmYIoUSRVQzK/view?usp=sharing

test.py releases a list of tags. Tag accuracy filter is kept at 70%. 

results.py then generate the sugesstions for each business. 
