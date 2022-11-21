type_defs = """
    union TestUnion = Partner | Network | Publisher
    
    type Partner {
        name: String
        subtype: String
        value_test_partner: String!
    }
    type Network {
        name: String
        subtype: String
        value_test_network: Boolean!
    }
    type Publisher {
        name: String
        subtype: String
        value_test_publisher: Int!
    }
    
    type Result {
        test: String
        elo: TestUnion
    }
    
    type Query {
        hello: [Result]
    }
"""