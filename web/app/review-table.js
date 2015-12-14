import React from "react";

export default class ReviewTable extends React.Component{
  render() {
    const reviews = this.props.reviews;
    return (
      <div className="reviews-table">
        <table className="table text-left" style={{width: "80%", margin: "0 auto"}}>
          <tbody>
            <tr>
              <th>Rank</th>
              <th>Name</th>
              <th>Keywords</th>
              <th>Score</th>
            </tr>
            {reviews &&
              reviews.map((review) => {
                return <tr>
                        <td>{review.rank}</td>
                        <td>{review.name}</td>
                        <td>
                          <a href={review.keywords}><img width="150" height="150" src={review.keywords}/></a>
                        </td>
                        <td>{review.score}</td>
                      </tr>
              })
            }
          </tbody>
        </table>
      </div>
    );
  }
}
