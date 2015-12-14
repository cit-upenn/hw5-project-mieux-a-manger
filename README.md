# hw5-project-mieux-a-manger

I. 	Project scope

This project aims to generate top 5 restaurants in Las Vegas based on Yelp reviews. More specifically, we give reviews different weightings based on the reviewer's expertise in a particular cuisine. As a results, our score will be more "authentic" than the raw average score used by Yelp. For this particular project, we will only consider six different cuisine: Chinese, Indian, Japanese, Korean, Vietnamese and Thai. 

II. 	Data & datasets

Data source: Yelp Dataset Challenge Round 6 (JSON)
http://www.yelp.co.uk/dataset_challenge

Cleansed Datasets:
	i 	business_subset		18	KB 
	ii 	review_subset		4.7 MB 
	iii 	user_subset		17	MB 

	i. 	business_subset
		- Subset of the business data
		- Will link this data via unique ID to review
		- Filters:
			city:		Las Vegas
			categories:	'Chinese', 'Indian', 'Japanese', 'Korean', 'Vietnamese', 'Thai'
			reviews:	> 100
			stars:		>= 4.0
	
	ii. review_subset
		- Subset of the review data:
			Review records for all restaurants selected in i, regardless of the user
		- Reviews are linked with business by business ID and with user by user ID
	
	iii.user_subset
		- Subset of the user data:
			Distinct users of all review records selected

III.	Web framework / UI
	React web page styled with bootstrap. See user manual on how to load the page using webpack.
	The UI has a simple drop down list to choose the cuisine in interest.

	

