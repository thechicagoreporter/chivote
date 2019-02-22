import React, { Component } from 'react';
import { FormattedMessage, injectIntl } from 'react-intl';
import decode from 'decode-html';
import Parser from 'html-react-parser';
import { Helmet } from 'react-helmet';
import { Breadcrumb, Page } from 'Components/common';
import './style.scss';

String.prototype.capitalize = function() {
  return this.charAt(0).toUpperCase() + this.slice(1);
};

function FormattedMessageFixed(props) {
  return <FormattedMessage {...props} />;
}

class ContentItemDetail extends Component {
  render() {
    const { title, slug, content, helmet, background } = this.props;
    let pageContent = Parser(decode(content.replace(/"'|'"/g, '"'))); // fixing bad quotes that were breaking links

    if (slug == 'quiz' && typeof window !== `undefined`) {
      var { ReactTypeformEmbed } = require('react-typeform-embed');

      pageContent = (
        <div
          className='column is-full'
          style={{ height: '500px', position: 'relative' }}
        >
          <ReactTypeformEmbed
            buttonText={this.props.intl.locale === 'es' ? 'Empezar' : 'Start'}
            url={
              this.props.intl.locale === 'es'
                ? 'https://starlyn.typeform.com/to/UFJDYa'
                : 'https://starlyn.typeform.com/to/WdZTNE'
            }
            style={{ height: '500px' }}
          />
        </div>
      );
    }

    if (slug == 'faq') {
      require('./PageFaq.scss');
    }

    var classes = `container page-${slug}`;

    const titles = {
      faq: 'FAQ'
    };

    const activeLabel = (
      <FormattedMessageFixed
        id={`common.link.${slug}`}
        defaultMessage={titles[slug] || slug.capitalize()}
      />
    );

    return (
      <>
        <Helmet>
          <style>{`body { background: ${background} !important; }`}</style>
          {Parser(decode(helmet))}
        </Helmet>
        <Page childClass={classes}>
          <div className={'columns is-multiline is-centered'}>
            <Breadcrumb className='column is-full' activeLabel={activeLabel} />
            <h1 className='column is-full page-heading title'>{title}</h1>
            {pageContent}
          </div>
        </Page>
      </>
    );
  }
}

export default injectIntl(ContentItemDetail);