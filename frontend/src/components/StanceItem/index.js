import React from 'react';
import moment from 'moment-mini';
import decode from 'decode-html';
import Parser from 'html-react-parser';

import {
  Accordion,
  AccordionItem,
  AccordionItemTitle,
  AccordionItemBody
} from 'react-accessible-accordion';

import 'react-accessible-accordion/dist/minimal-example.css';
import './style.scss';

const StanceItem = props => {
  const { candidate } = props;
  const { date, link, source, statement_long, statement_short } = props.data;

  return (
    <Accordion>
      <AccordionItem className="accordion__item list-item article-item stance__item">
        <AccordionItemTitle className="accordion__title row row--main u-position-relative">
          <div className="candidate-item__text-main">
            <img
              src={candidate.br_thumb_url}
              alt=""
              className="candidate-item__img mb-1"
            />
            <span className="is-lightblue-text is-lbs is-size-4">
              {candidate.full_name}
            </span>
            <p>
              <strong className="has-text-white">{statement_short}</strong>
            </p>
          </div>

          <cite className="has-text-right candidate-item__text-secondary">
            <a href={link}>
              {date && moment(date).format('MMM D, YYYY') + ' • '}
              {source}
            </a>
          </cite>

          <div className="accordion__arrow" role="presentation" />
        </AccordionItemTitle>
        <AccordionItemBody className="accordion__body row row--secondary">
          <blockquote className="has-text-white is-futura mb-1">
            {Parser(decode(statement_long))}
          </blockquote>
        </AccordionItemBody>
      </AccordionItem>
    </Accordion>
  );
};

export default StanceItem;