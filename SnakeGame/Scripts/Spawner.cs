using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawner : MonoBehaviour
{
    [SerializeField] GameObject itemToSpawn;
    [SerializeField] Vector3 topLeftBound;
    [SerializeField] Vector3 bottomRightBound;
    [SerializeField] float minTimeToSpawn = 10f;
    [SerializeField] float maxTimeToSpawn = 30f;
    [SerializeField] int maxItemsAtOnce = 1;

    int currentItemsSpawned;

    GameController gameController;
    GameObject[] walls;

    private void Start()
    {
        FindWallObjects();
    }

    void SpawnItem()
    {
        Vector3 attemptedSpawnLocation = GetRandomizedVector();
        if (CheckSnakeVectorOverlap(attemptedSpawnLocation) &
            CheckPointObjectVectorOverlap(attemptedSpawnLocation) &
            CheckWallsVectorOverlap(attemptedSpawnLocation))
        {
            GameObject item = Instantiate(GetItemToSpawn(), attemptedSpawnLocation,
                            Quaternion.identity);
            item.transform.parent = transform;
        }
    }

    public Vector3 GetRandomizedVector()
    {
        var x = Mathf.Round(Random.Range(topLeftBound.x, bottomRightBound.x));
        var y = Mathf.Round(Random.Range(bottomRightBound.y, topLeftBound.y));
        var z = 0;
        return new Vector3(x, y, z);
    }

    bool CheckSnakeVectorOverlap(Vector3 attempt)
    {
        SnakeSegment[] segments = FindObjectsOfType<SnakeSegment>();
        foreach (SnakeSegment segment in segments)
        {
            if (attempt == segment.transform.position)
            {
                return false;
            }
        }
        return true;
    }

    bool CheckWallsVectorOverlap(Vector3 attempt)
    {
        foreach (GameObject wall in walls)
        {
            if (wall.GetComponent<Collider2D>().bounds.Contains(attempt))
            {
                return false;
            }
        }
        return true;
    }

    bool CheckPointObjectVectorOverlap(Vector3 attempt)
    {
        PointObject[] pointObjects = FindObjectsOfType<PointObject>();
        foreach (PointObject pointObject in pointObjects)
        {
            if (attempt == pointObject.transform.position)
            {
                return false;
            }
        }
        return true;
    }

    public bool CanSpawn()
    {
        return transform.childCount < maxItemsAtOnce;
    }

    private void FindWallObjects()
    {
        walls = GameObject.FindGameObjectsWithTag("Walls");
        gameController = FindObjectOfType<GameController>();
        StartCoroutine(StartSpawning());
    }

    public GameObject GetItemToSpawn()
    {
        return itemToSpawn;
    }

    public float GetRandomTimeToSpawn()
    {
        return Random.Range(minTimeToSpawn, maxTimeToSpawn);
    }

    public float GetMinTimeToSpawn()
    {
        return minTimeToSpawn;
    }

    public float GetMaxTimeToSpawn()
    {
        return maxTimeToSpawn;
    }

    IEnumerator StartSpawning()
    {
        while (gameController.IsPlaying())
        {
            yield return new WaitForSeconds(GetRandomTimeToSpawn());
            if (CanSpawn()) { SpawnItem(); }

        }
    }
}
