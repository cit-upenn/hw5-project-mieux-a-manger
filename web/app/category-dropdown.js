import React from "react";

export default class CategoryDropdown extends React.Component{
  constructor(){
    super();
    this.state = {category: null}
  }
  handleCategoryChange(e){
    let category;
    category = e.target.value;

    this.setState({value: category});
    this.props.updateReviews(category);
  }
  render() {
    return (
      <div style={{marginBottom: "25px"}}className="category-dropdown text-center">
        <select className="form-control" style={{width: "250px", margin: "0 auto"}} onChange={this.handleCategoryChange.bind(this)} value={this.state.category}>
          <option>Choose a type of cuisine</option>
          <option value="chinese">Chinese</option>
          <option value="indian">Indian</option>
          <option value="japanese">Japanese</option>
        </select>
      </div>
    );
  }
}
