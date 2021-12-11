//Banker's Algorithm
//은행원 알고리즘
 
#include<iostream>
#include<cstdio>
#define R_LEN 4
#define PROCESS_CNT 5
using namespace std;
 
//======================//
 
class process{
private:
    bool finish;    //process가 자원을 할당 받고 작업을 완료했는지
    int maxResource[R_LEN];   //process가 최대로 필요로 하는 자원의 개수
    int allocation[R_LEN];    //process가 현재 가지고 있는 자원들
    int need[R_LEN];  //process가 작업을 완료하기 위해 필요한 자원의 개수 (max-allocation)
public:
    process(int allocation[R_LEN], int maxResource[R_LEN]){
        finish = false;
        for(int i=0; i<R_LEN; i++){
            this->maxResource[i] = maxResource[i];
            this->allocation[i] = allocation[i];
            this->need[i] = this->maxResource[i] - this->allocation[i];
        }
    }
 
    bool isFinish() const{
        return finish;
    }
    void setFinish(bool finish){
        this->finish = finish;
    }
 
    bool isWork(int *available) const{ //work가 가능한지
        for(int i=0; i<R_LEN; i++){
            if(need[i] <= available[i]) continue;
            return false;
        }
        return true;
    }
 
    void giveAllocation(int *available){
        for(int i=0; i<R_LEN; i++){
            available[i] += allocation[i];
        }
    }
    void printAllocation() const{
        cout << "allocation : ";
        for(int i=0; i<R_LEN; i++){
            printf("%d ", allocation[i]);
        }
        printf("\n");
    }
    void printMaxResource() const{
        cout << "maxResource : ";
        for(int i=0; i<R_LEN; i++){
            printf("%d ", maxResource[i]);
        }
        printf("\n");
    }
    void printNeed() const{
        cout << "need : ";
        for(int i=0; i<R_LEN; i++){
            printf("%d ", need[i]);
        }
        printf("\n");
    }
    void printAll() const{
        printAllocation();
        printMaxResource();
        printNeed();
        printf("\n");
    }
};
 
//======================//
 
void printProcess(process *p[PROCESS_CNT]){
    for(int i=0; i<PROCESS_CNT; i++){
        printf("p[%d]\n", i);
        p[i]->printAll();
    }
}
void printAvailable(int *available){
    cout << "available : ";
    for(int i=0; i<R_LEN; i++){
        printf("%d ", available[i]);
    }
    printf("\n");
}
void printResult(bool result, int *sequence){
    printf("\nresult\n");
    if(result){
        for(int i=0; i<5; i++){
            printf("process[%d]", sequence[i]);
            if(i!=4) printf(" -> ");
        }
        printf("\n");
    }else{
        cout << "Fail" << endl;
    }
 
}
 
//======================//
//safety algorithm.
bool isSafe(process *p[PROCESS_CNT]){
    for(int i=0; i<PROCESS_CNT; i++){
        if(p[i]->isFinish()) continue;  //각각의 프로세스의 작업이 완료되었는지
        return false;
    }
 
    //모든 프로세스의 작업이 true이면
    return true;
}
 
//Banker's Algorithm
bool bankers(process *p[PROCESS_CNT], int *available, int *sequence){
    printProcess(p);
 
 
    for(int i=0; i<PROCESS_CNT; i++){
        for(int j=0; j<PROCESS_CNT; j++){
 
            if(!p[j]->isFinish() && p[j]->isWork(available)){//Finish[i] == false && need<= work
                p[j]->setFinish(true);
                p[j]->giveAllocation(available);
 
                printAvailable(available);  //available 출력
                sequence[i] = j;
                break;
            }
        }
    }
    return isSafe(p);
}
 
//======================//
 
int main(void){
    int sequence[PROCESS_CNT]={0};  //프로세스 수행 순서 저장을 위한 배열
 
    //초기 setting //
 
    int available[R_LEN] = {3,2,1,1}; //resource available.
    int allocation[PROCESS_CNT][R_LEN] = {{4,0,0,1}, {1,1,0,0}, {1,2,5,4}, {0,6,3,3},{0,2,1,2}};
    int maxResource[PROCESS_CNT][R_LEN] = {{6,0,1,2}, {1,7,5,0}, {2,3,5,6}, {1,6,5,3}, {1,6,5,6}};
    /*
    int available[R_LEN] = {3,3,2}; //resource available.
    int allocation[PROCESS_CNT][R_LEN] = {{0,1,0}, {2,0,0}, {3,0,2}, {0,0,0},{0,0,2}};
    int maxResource[PROCESS_CNT][R_LEN] = {{7,5,3}, {3,2,2}, {9,0,2}, {2,2,2}, {4,3,3}};
    */
    process *p[PROCESS_CNT];
    for(int i=0; i<PROCESS_CNT; i++){
        p[i] = new process(allocation[i], maxResource[i]);
    };
    //============//
    bool result = bankers(p, available, sequence);
    printResult(result, sequence);
    //============//
    for(int i=0; i<PROCESS_CNT; i++){
        delete p[i];
    }
    return 0;
}

