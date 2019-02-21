import React from 'react';
import Parser from 'html-react-parser';
import decode from 'decode-html';
import moment from 'moment-mini';
import './style.scss';

const ArticleItem = props => {
  const { fields } = props.data;
  const extraClasses = props.ClassName ? ' ' + props.className : '';

  return (
    <div className={`list-item article-item${extraClasses}`}>
      <div className='article-item__meta is-flex flex-space-between mb-1 is-fullwidth'>
        <div>
          <span className='has-text-grey-lighter'>
            {moment(fields.date).format('MMM D, YYYY')}
          </span>
          <time dateTime={fields.date} className='is-hidden'>
            {fields.date}
          </time>
        </div>
        <cite className='article-item__source is-lightblue-text has-text-right'>
          {fields.source}
        </cite>
      </div>
      <a
        className='article-item__headline has-text-white mb-1'
        href={fields.link}
      >
        {fields.hed}
      </a>
      <p className='has-text-grey-lighter'>
        {fields.summary &&
          Parser(decode(fields.summary).replace(/<(?:.|\n)*?>/gm, ''))}
      </p>
    </div>
  );
};

export default ArticleItem;