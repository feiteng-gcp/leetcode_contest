

class Solution {
public:
    int racecar(int target) {
        
        deque< vector<int> > queue;
        queue.push_back( {0, 1, 0, 0} ); //position, speed, action(1 for A, 2 for R), steps
        
        unordered_map<int, unordered_set<int> > hash;
        hash[0].insert(1);
        
        //set< vector<int> > hash;
        //hash.insert( {0, 1} );
        
        int curIndex = 0;
        while (queue.size() > 0 )
        {
            vector<int> cur = queue.front();
            int pos   = cur[0];
            int speed = cur[1];                        
            int nextSteps = cur[3] + 1;
            queue.pop_front();
                                                         
            if ( hash[pos+speed].find( speed * 2 ) == hash[pos+speed].end() && abs(speed) < target * 2 && pos < 2 * target && pos > 2 * -target)
            {               
                queue.push_back( {pos + speed, speed * 2, 1, nextSteps} );
                hash[pos+speed].insert( speed * 2 );
                if (pos + speed == target) return nextSteps;
            }
            
            //R
            if (speed > 0)
            {
                if ( hash[pos].find( -1 ) == hash[pos].end() )
                {
                    queue.push_back( {pos, -1, 2, cur[3] + 1} );
                    hash[pos].insert( -1 );                    
                }
            }
            else 
            {
                if ( hash[pos].find( 1 ) == hash[pos].end() )
                {
                    queue.push_back( {pos, 1, 2, cur[3] + 1} );    
                    hash[pos].insert( 1 ); 
                }                
            }
            
            
            //A                  
            /*
            if ( hash.find( {pos+speed, speed * 2} ) == hash.end() )
            {               
                queue.push_back( {pos + speed, speed * 2, 1, nextSteps} );
                hash.insert( {pos+speed, speed * 2} );
                if (pos + speed == target) return cur[3] + 1;                
            }
            
            //R
            if (speed > 0)
            {
                if ( hash.find( {pos, -1} ) == hash.end() )
                {
                    queue.push_back( {pos, -1, 2, cur[3] + 1} );
                    hash.insert( {pos, -1} );
                }
            }
            else 
            {
                if ( hash.find( {pos, 1} ) == hash.end() )
                {
                    queue.push_back( {pos, 1, 2, cur[3] + 1} );    
                    hash.insert( {pos, 1} );
                }                
            }
            */
        }                
    }
};