import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import RaceDetail from './pages/RaceDetail';
import RaceList from './pages/RaceList';
import CandidateDetail from './pages/CandidateDetail';
import ContentItemDetail from './pages/ContentItemDetail';

/**
 * Maintain a simple map of React components to make it easier for
 * Django to reference individual components.
 */

const pages = {
  App,
  RaceDetail,
  RaceList,
  CandidateDetail,
  ContentItemDetail
};

/**
 * If Django hasn't injected these properties into the HTML
 * template that's loading this script then we're viewing it
 * via the create-react-app liveserver
 */
window.component = window.component || 'App';
window.props = window.props || { env: 'create-react-app' };
window.reactRoot = window.reactRoot || document.getElementById('root');

ReactDOM.render(
  React.createElement(pages[window.component], window.props),
  window.reactRoot
);
