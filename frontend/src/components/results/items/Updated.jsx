import React from 'react';
import { FormattedMessage, injectIntl } from 'react-intl';
import moment from 'moment';

const Updated = props => {
  const { className, datetime, isLoading } = props;
  const { locale } = props.intl;

  if (isLoading) {
    return (
      <div className={className}>
        <FormattedMessage
          id='Results.Updated.loading'
          defaultMessage='Checking for new results...'
        />
      </div>
    );
  } else {
    return (
      <div className={className}>
        <FormattedMessage
          id='Results.Updated.text'
          defaultMessage='Last updated: {datetime}'
          values={{
            datetime: moment(datetime)
              .locale(locale)
              .format('lll')
          }}
        />
      </div>
    );
  }
};

export default injectIntl(Updated);
