using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class InputController : MonoBehaviour
{
    [SerializeField] Vector2 startingDirection = Vector2.right;
    Vector2 direction;
    Vector2 nextDirection;
    bool moveExecuted = true;

    private void Start()
    {
        nextDirection = startingDirection;
    }

    public void MoveExecuted()
    {
        // This exists to stop the snake being able to move into it's self if input was too fast 
        moveExecuted = true;
    }

    public Vector2 GetInput()
    {
        {
            if (Input.GetKeyDown(KeyCode.UpArrow))
            {
                nextDirection = Vector2.up;
            }

            else if (Input.GetKeyDown(KeyCode.DownArrow))
            {
                nextDirection = Vector2.down;
            }

            else if (Input.GetKeyDown(KeyCode.LeftArrow))
            {
                nextDirection = Vector2.left;
            }

            else if (Input.GetKeyDown(KeyCode.RightArrow))
            {
                nextDirection = Vector2.right;
            }

            if (direction + nextDirection != Vector2.zero & moveExecuted)
            {
                direction = nextDirection;
                moveExecuted = false;
                return nextDirection;
                
            }
            return direction;
        }
    }
}
