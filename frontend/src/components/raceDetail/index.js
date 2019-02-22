import React, { Component } from 'react';
import { FormattedMessage, injectIntl } from 'react-intl';
import { slide as SlideView } from 'react-burger-menu';
import CandidateView from './CandidateView';
import {
  ArticleFeed,
  CandidateFeed,
  EventFeed,
  FinanceFeed,
  StanceFeed
} from './feeds';
import { parseHtml } from 'Components/utils';
import { Breadcrumb, Page } from 'Components/common';
import './styles.scss';

function FormattedMessageFixed(props) {
  return <FormattedMessage {...props} />;
}

class RaceDetail extends Component {
  constructor(props) {
    super(props);
    this.state = {
      feed: this.props.feed ? this.props.feed : 'candidates',
      currentCandidate: null,
      slideViewActive: false
    };
  }

  setCandidateView = candidateObj => {
    this.setState({
      slideViewActive: true,
      currentCandidate: candidateObj
    });
  };

  unsetCandidateView = state => {
    this.setState({
      slideViewActive: state.isOpen
    });
  };

  componentDidMount() {
    const currPath = window.location.pathname;
    const raceSlug = this.props.data.slug;

    let url = currPath.split(raceSlug)[0];
    url += raceSlug + '/';
    url += this.state.feed + '/';

    window.history.pushState({}, null, url);
  }

  componentDidUpdate() {
    this.componentDidMount();
  }

  renderFeed = () => {
    if (this.state.feed === 'candidates') {
      return (
        <CandidateFeed
          candidates={JSON.parse(this.props.candidates)}
          handleClick={this.setCandidateView}
        />
      );
    } else if (this.state.feed === 'articles') {
      return (
        <ArticleFeed
          articles={JSON.parse(this.props.data.articles)}
          feed_url={`/races/${this.props.data.slug}/rss.xml`}
        />
      );
    } else if (this.state.feed === 'stances') {
      return (
        <StanceFeed
          stances={JSON.parse(this.props.data.stances)}
          issues={JSON.parse(this.props.data.issues)}
          candidates={JSON.parse(this.props.candidates)}
        />
      );
    } else if (this.state.feed === 'events') {
      return <EventFeed slug={this.props.data.documenters_slug} />;
    } else if (this.state.feed === 'finances') {
      return <FinanceFeed candidates={JSON.parse(this.props.candidates)} />;
    }
  };

  renderButtons = () => {
    const officeName = JSON.parse(this.props.data.office).office;

    const FeedButton = props => {
      var enabled = 'enabled' in props ? props.enabled : true;

      if (enabled) {
        return (
          <div className='control column is-one-third'>
            <button
              className={`button is-rounded is-large is-${props.slug}`}
              onClick={() => this.setState({ feed: props.slug })}
            >
              {/* Events */}
              <span className='icon'>
                <i className={`fa fa-lg ${props.icon}`} />{' '}
              </span>
              <span className='button__label is-hidden-mobile'>
                <FormattedMessageFixed
                  id={`RaceDetail.button.${props.slug}`}
                  defaultMessage={props.label}
                />
              </span>
            </button>
          </div>
        );
      } else {
        return null;
      }
    };

    const buttons = [
      {
        slug: 'candidates',
        label: 'Candidates',
        icon: 'fa-user-tie'
      },
      {
        slug: 'articles',
        label: 'Articles',
        icon: 'fa-newspaper'
      },
      {
        slug: 'stances',
        label: 'Stances',
        icon: 'fa-comment-dots',
        enabled: officeName.includes('Mayor') || officeName.includes('Alcalde')
      },
      {
        slug: 'events',
        label: 'Events',
        icon: 'fa-calendar'
      },
      {
        slug: 'finances',
        label: 'Finances',
        icon: 'fa-money-check-alt'
      }
    ];

    return (
      <div
        className={`is-${
          this.state.feed
        }-active toggle-feed columns is-mobile is-multiline`}
      >
        {buttons.map((d, i) => {
          return <FeedButton {...d} key={i} />;
        })}
      </div>
    );
  };

  render() {
    const { description, office, slug } = this.props.data;
    const officeName = JSON.parse(office).office;

    let currPage;

    if (typeof window !== `undefined`) {
      const currPath = window.location.pathname;
      currPage = currPath.split(slug)[0] + slug + '/';
    } else {
      currPage = '/';
    }

    return (
      <>
        <SlideView
          left
          width={320}
          isOpen={this.state.slideViewActive}
          onStateChange={this.unsetCandidateView}
          customBurgerIcon={false}
        >
          {this.state.currentCandidate && (
            <CandidateView
              apiUrl={this.props.ballot_ready_api_url}
              data={this.state.currentCandidate}
            />
          )}
        </SlideView>

        <Page childClass='container page--detail' sectionClass='race-detail'>
          <Breadcrumb activePath={currPage} activeLabel={officeName} />
          <h1 className='page-heading title is-3'>
            <FormattedMessage
              id='RaceDetail.heading'
              defaultMessage='Race for {officeName}'
              values={{ officeName }}
            />
          </h1>
          {parseHtml(description, [[/"'|'"/g, '"']])}
          {this.renderButtons()}
          {this.renderFeed()}
        </Page>
      </>
    );
  }
}

export default injectIntl(RaceDetail);