import React, { Component } from 'react';
import ResultsTable from './ResultsTable';
import moment from 'moment-mini';
import * as resultsJson from './results.tmp.json';

const PrecinctsReportingText = ({
  precinctsReporting,
  precinctsTotal,
  lastUpdated
}) => (
  <p className='small'>
    {precinctsReporting} of {precinctsTotal} precincts reporting.
  </p>
);

class ResultsFeed extends Component {
  constructor(props) {
    super(props);

    const results = resultsJson.default;

    const contest = results.contests[props.cboeId];
    const precinctsReporting =
      contest.meta[results.contest_headers.indexOf('# Completed precincts')];
    const precinctsTotal =
      contest.meta[results.contest_headers.indexOf('# of Eligible Precincts')];
    const lastUpdated = results.datetime;

    this.state = {
      dataHeaders: results.cand_headers,
      dataClasses: results.cand_classes,
      data: contest.cands,
      precinctsReporting,
      precinctsTotal,
      lastUpdated,
      drawBars: props.drawBars
    };
  }

  render() {
    return (
      <div className='contest'>
        <PrecinctsReportingText {...this.state} />
        <ResultsTable {...this.state} appendBarKey='append-bar' />
      </div>
    );
  }
}

export default ResultsFeed;
