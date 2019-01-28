import React, { Component } from 'react';
import Page from 'Components/Page';
import List from 'Components/List';
import WardLookup from 'Components/WardLookup';

class RaceList extends Component {
  state = {
    showLookup: false
  };

  render() {
    const parsedRaceData = JSON.parse(this.props.data.races);
    const copyRaceData = [...parsedRaceData];
    const extractWardData = [];

    console.log(parsedRaceData.length);

    for (let i = 0; i < parsedRaceData.length; i++) {
      const race = parsedRaceData[i];

      if (race.name.toLowerCase().indexOf('ward') > -1) {
        extractWardData.push(race);
        copyRaceData[i] = null;
      }
    }

    const flattenRemains = copyRaceData.filter(x => (x ? true : false));

    const wardButtons = extractWardData.map(data => (
      <li className="column is-4">
        <WardButton key={data.id} data={data} />
      </li>
    ));

    const otherRaces = flattenRemains.map(data => (
      <li className="column">
        <a key={data.id} href={`${data.id}`} className="ward-button">
          {data.name}
        </a>
      </li>
    ));

    const races = JSON.parse(this.props.data.races);
    return (
      <div>
        <Page
          className="page page--detail page--inner container"
          heading="Races"
        >
          <p className="is-lsb">
            Choose a specific race to get more information and view candidates.
          </p>
          <List className="columns">{otherRaces}</List>
          <h2 className="page-heading title is-4">Aldermanic</h2>
          <p className="is-lsb">
            Choose a specific ward number to get more information and view
            candidates.
          </p>
          {!this.state.showLookup && (
            <button
              className="button is-rounded mb-1 is-fullwidth"
              onClick={() => this.setState({ showLookup: true })}
            >
              I don't know my ward
            </button>
          )}
          {this.state.showLookup && (
            <div className="list-item">
              <WardLookup />
            </div>
          )}
          <List className="columns is-mobile is-multiline">{wardButtons}</List>
        </Page>
      </div>
    );
  }
}

const WardButton = props => (
  <a href={`${props.data.id}`} className="ward-button">
    {props.data.name.match(/\d+/)}
  </a>
);

export default RaceList;
