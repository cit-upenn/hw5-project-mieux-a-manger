import React from "react";
import CategoryDropdown from "./category-dropdown"
import ReviewTable from "./review-table"
const Reviews = require('json!../reviews.json');


export default class ReviewPage extends React.Component {
  constructor(){
    super();
    this.state = {reviews: []}
  }
  updateReviews(category) {
    this.setState({reviews: Reviews[category]})
  }
  render() {
    return (
      <div className="review-page">
        <h1>Top Restaurants in Las Vegas</h1>
        <CategoryDropdown updateReviews={this.updateReviews.bind(this)}/>
        <ReviewTable reviews={this.state.reviews}/>
      </div>
    );
  }
}
