using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PointObject : MonoBehaviour
{
    [SerializeField] int points = 1;
    [SerializeField] float despawnTime = 0;

    float timer;
    bool canDie;

    void Start()
    {
        canDie = despawnTime > 0;
    }

    void Update()
    {
        if (canDie)
        {
            TimerTick();
        }
    }

    private void TimerTick()
    {
        timer += Time.deltaTime;
        if (timer >= despawnTime)
        {
            Kill();
        }
    }

    private void Kill()
    {
        Destroy(gameObject);
    }

    public int GetPoints()
    {
        return points;
    }
}
