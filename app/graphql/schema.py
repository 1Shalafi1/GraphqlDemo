model_type_defs = """
    type Actor {
        actor_id: ID!
        first_name: String!
        last_name: String!
        
        last_update: String!
    
        films(limit: Int = 2, skip: Int = 0): [Film]
        
        
    }
    
    type Film {
        film_id: ID!
        language_id: Int

        title: String!
        description: String!
        release_year: String!
        rental_duration: Float!
        rental_rate: String!
        length: Int
        replacement_cost: Float
        rating: String!
        special_features: [String]
        fulltext: [String]

        last_update: String!

        actors(limit: Int = 0, skip: Int = 0): [Actor]
    }
    
"""

query_type_defs = """
    type Query {
        actors(skip: Int = 0, limit: Int = 10): [Actor]!
        films(skip: Int = 0, limit: Int = 10): [Film]!
    }
"""


compiled_schema = "\n\n".join(x for x in (model_type_defs, query_type_defs))