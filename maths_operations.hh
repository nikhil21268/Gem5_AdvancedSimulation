#ifndef MATHS_OPERATIONS_HH
#define MATHS_OPERATIONS_HH

#include "params/MathsOperations.hh"
#include "sim/sim_object.hh"

namespace gem5 {

class MathsOperations : public SimObject {
  
  private:
    void processEvent();
    void processEvent1();
    void processEvent2();
    void processEvent3();

    EventFunctionWrapper event;

    EventFunctionWrapper fibEvent;
    EventFunctionWrapper primeEvent;
    EventFunctionWrapper gcdEvent;

  
  public:
    MathsOperations(const MathsOperationsParams &p);

    void startup() override;

};

} // namespace gem5

#endif // MATHS_OPERATIONS_HH