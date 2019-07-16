import { ApolloServer, gql } from 'apollo-server-micro'

const typeDefs = gql`
  type Query {
    hello: String
  }
`

const resolvers = {
  Query: {
    hello: () => 'world',
  },
}

const apolloServer = new ApolloServer({ typeDefs, resolvers })

export default apolloServer.createHandler({ path: '/api' })
export const config = {
  api: {
    bodyParser: false,
  },
}
