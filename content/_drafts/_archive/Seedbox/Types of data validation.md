This reading describes the purpose, examples, and limitations of six types of data validation. The first five are validation types associated with the data (type, range, constraint, consistency, and structure) and the sixth type focuses on the validation of application code used to accept data from user input. 

As a junior data analyst, you might not perform all of these validations. But you could ask if and how the data was validated before you begin working with a dataset. Data validation helps to ensure the integrity of data. It also gives you confidence that the data you are using is clean. The following list outlines six types of data validation and the purpose of each, and includes examples and limitations.

![Icon of a question mark with the words data type](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/bwKS3nJvQoqCkt5yb2KKtg_381561b0be794604bbab4b371ca61bc9_Screen-Shot-2021-02-08-at-5.22.06-PM.png?expiry=1688601600000&hmac=Bpn5QI53gR1Ac9gF-T4LEksHDy-3kbeSPP8hsKeoX_8)

- **Purpose**: Check that the data matches the data type defined for a field.
    
- **Example**: Data values for school grades 1-12 must be a numeric data type.
    
- **Limitations**: The data value 13 would pass the data type validation but would be an unacceptable value. For this case, data range validation is also needed.
    

![Icon of a man holding a magnifying glass with words data range](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/dPyj72GhQXS8o-9hoTF0Ag_839574976de44a4b9a3ec45f4e4e36e2_Screen-Shot-2021-02-08-at-5.25.03-PM.png?expiry=1688601600000&hmac=WS2v3EV0qG54-XOYTzYsC9wQlh8De9zT1lUz00PU_A0)

- **Purpose**: Check that the data falls within an acceptable range of values defined for the field.
    
- **Example**: Data values for school grades should be values between 1 and 12.
    
- **Limitations**: The data value 11.5 would be in the data range and would also pass as a numeric data type. But, it would be unacceptable because there aren't half grades. For this case, data constraint validation is also needed.
    

![Icon with gears and the words data constraints](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/DUa8GZEkTR6GvBmRJC0emw_a9e6271e8f1c4cb0820ec3d6ee34f4eb_Screen-Shot-2021-02-08-at-5.27.40-PM.png?expiry=1688601600000&hmac=r8D_6DVVsu864TUrncttVvN8f7yzvsVeiJJDOQLrGW4)

- **Purpose**: Check that the data meets certain conditions or criteria for a field. This includes the type of data entered as well as other attributes of the field, such as number of characters.
    
- **Example**: Content constraint: Data values for school grades 1-12 must be whole numbers.
    
- **Limitations**: The data value 13 is a whole number and would pass the content constraint validation. But, it would be unacceptable since 13 isn’t a recognized school grade. For this case, data range validation is also needed.
    

![Icon of a traffic light with words data consistency](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Xlu9FFgIRDGbvRRYCFQx-w_6eaa5307239541e9a5e0c77a343f9c8b_Screen-Shot-2021-02-08-at-5.30.56-PM.png?expiry=1688601600000&hmac=nFO6I7j0AivVfenvF7BslI6fw4UggFELJfEidyMZjlo)

- **Purpose**: Check that the data makes sense in the context of other related data.
    
- **Example**: Data values for product shipping dates can’t be earlier than product production dates.
    
- **Limitations**: Data might be consistent but still incorrect or inaccurate. A shipping date could be later than a production date and still be wrong.
    

![Icon of a clipboard checklist with words Data structure](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/6kdSdq1vQfeHUnatbwH3Lg_02d9444056b340e58377aa792ecb0d43_Screen-Shot-2021-02-08-at-5.33.03-PM.png?expiry=1688601600000&hmac=edVOAa7jqpO7ic0Pyl7CdWlXQkztfKoENB3tg7U5VzQ)

- **Purpose**: Check that the data follows or conforms to a set structure.
    
- **Example**: Web pages must follow a prescribed structure to be displayed properly.
    
- **Limitations**: A data structure might be correct with the data still incorrect or inaccurate. Content on a web page could be displayed properly and still contain the wrong information.
    

![Icon with computer arrows traveling to multiple users with the word Code validation](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Saof9D7aT8eqH_Q-2k_Hyg_d144822d70ac4ec3b22b5126c0b32e60_Screen-Shot-2021-02-08-at-5.34.42-PM.png?expiry=1688601600000&hmac=EYn2ZtSz8KY7xubUZtZfZsBFJGNrF1OFNiV8zQ5Uj9Y)

- **Purpose:** Check that the application code systematically performs any of the previously mentioned validations during user data input.
    
- **Example:** Common problems discovered during code validation include: more than one data type allowed, data range checking not done, or ending of text strings not well defined.
    
- **Limitations:** Code validation might not validate all possible variations with data input.