class Solution {
public:
    
    #define mp make_pair
    #define pii pair<int,int>
    
    struct Data{
        int pos,  dist,  speed;
        Data( int p , int d , int s): pos(p) , dist(d), speed(s){}
        Data(){}
    };
    
    int racecarBrute(int target, int initial) {
        queue<Data> Q;
        set<pii> seen;
        Q.push(Data(initial, 0, -1));
        seen.insert(mp(initial, -1));
        while( !Q.empty() ){
            Data p = Q.front(); Q.pop();
            int current = p.pos, distance = p.dist, speed = p.speed;
            //cout<<current<<" "<<distance<<" "<<speed<<endl;
            if( current == target ) return distance;
            
            pii A = mp(current + speed, speed * 2);
            if(A.first >= 0 && seen.find( A ) == seen.end() ){
                seen.insert(A);
                Q.push(Data( A.first, distance + 1, A.second ));
            }
            
            pii R = mp(current, -1);
            if( speed < 0 ) R.second = 1;
            if( seen.find( R ) == seen.end() ){
                seen.insert(R);
                Q.push(Data( R.first, distance + 1, R.second ));
            }
        }
        return 1<<30;
    }
    
    int racecar(int target){
        int initial = 0, p = 1;
        int left = 0, right = 0;
        int Rleft = 0, Rright = 0;
        int result = 0;
        for( ; ; ){  
            result++;
            initial += p;
            if( initial == target ) return result;
            if( initial > target ){
                left = initial - p;
                right = initial;
                Rright = result;
                Rleft = result - 1;
                break;
            }
            p *= 2;
        }
        //cout<<Rleft<<" "<<left<<" "<<" -- "<<Rright<<" "<<right<<endl;
        return 1 + min( Rleft + racecarBrute(target, left), Rright + racecarBrute(target,right));
        
    }
    
};