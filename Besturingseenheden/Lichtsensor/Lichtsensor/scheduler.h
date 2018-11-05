// Scheduler data structure for storing task data
typedef struct
{
	// Pointer to task
	void (* pTask)(void);
	// Initial delay in ticks
	unsigned int Delay;
	// Periodic interval in ticks
	unsigned int Period;
	// Runme flag (indicating when the task is due to run)
	unsigned char RunMe;
} sTask;

// Function prototypes
//-------------------------------------------------------------------

void scheduler_init_timer1(void);
void scheduler_start(void);
// Core scheduler functions
void scheduler_dispatch_tasks(void);
unsigned char scheduler_add_task(void (*)(void), const unsigned int, const unsigned int);
void scheduler_delete_task(const unsigned char);

// hier het aantal taken aanpassen ....!!
// Maximum number of tasks

#define SCHEDULER_MAX_TASKS (20)