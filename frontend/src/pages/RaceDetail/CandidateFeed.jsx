import React from 'react';
import _ from 'lodash';
import List from 'Components/List';
import CandidateItem from 'Components/CandidateItem';

const CandidateFeed = props => {
  const { candidates, handleClick } = props;

  return (
    <section id="the-candidates">
      <h2 className="is-hidden-tablet page-heading title is-4">Candidates</h2>
      <List className="candidates-list columns is-multiline is-0-mobile">
        {candidates.map(item => (
          <div className="column is-4">
            <CandidateItem
              key={item.pk}
              id={item.pk}
              handleClick={handleClick}
              data={item.fields}
            />
          </div>
        ))}
      </List>
    </section>
  );
};

export default CandidateFeed;