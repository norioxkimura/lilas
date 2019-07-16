import { ApolloClient } from 'apollo-client'
import { InMemoryCache } from 'apollo-cache-inmemory'
import { HttpLink } from 'apollo-link-http'
import { onError } from 'apollo-link-error'
import { ApolloLink } from 'apollo-link'
import fetch from 'isomorphic-unfetch'
import gql from 'graphql-tag'

const isBrowser = typeof window !== 'undefined'

const client = new ApolloClient({
  connectToDevTools: isBrowser,
  ssrMode: !isBrowser,
  link: ApolloLink.from([
    onError(({ graphQLErrors, networkError }) => {
      if (graphQLErrors)
        graphQLErrors.map(({ message, locations, path }) =>
          console.log(`[GraphQL error]: Message: ${message}, Location: ${locations}, Path: ${path}`),
        )
      if (networkError) console.log(`[Network error]: ${networkError}`)
    }),
    new HttpLink({
      uri: `http://${isBrowser ? process.env.APIHOST || 'localhost' : 'localhost'}:3000/api`,
      // note that this 'process.env.APIHOST' comes from next.config.js (build-time configuration, not run-time)
      // see : https://github.com/zeit/next.js#exposing-configuration-to-the-server--client-side
      fetch: !isBrowser && fetch,
    }),
  ]),
  cache: new InMemoryCache(),
})

const query = gql`
  {
    hello
  }
`

client.query({ query }).then(result => console.log(result))

const IndexPage = () => <h1>Testing Next.js App written in TypeScript</h1>

export default IndexPage
