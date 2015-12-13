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
      <div className="category-dropdown">
        <select onChange={this.handleCategoryChange.bind(this)} value={this.state.category}>
          <option value="chinese">Chinese</option>
          <option value="indian">Indian</option>
          <option value="japanese">Japanese</option>
          <option value="korean">Korean</option>
          <option value="vietnamese">Vietnamese</option>
          <option value="thai">Thai</option>
        </select>
      </div>
    );
  }
}
