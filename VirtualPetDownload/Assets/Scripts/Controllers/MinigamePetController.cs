using System;
using UnityEngine;

public class MinigamePetController : MonoBehaviour
{
    public float speed, jumpSpeed;
    private Rigidbody2D r2d;
    public bool grounded;

    private void OnEnable()
    {
        GetComponent<PetController>().enabled = false;
        GetComponent<NeedsController>().enabled = false;
        r2d = GetComponent<Rigidbody2D>();
        r2d.simulated = true;
    }

    private void OnDisable()
    {
        r2d.velocity = Vector3.zero;
        transform.position = Vector3.zero;
        r2d.simulated = false;
        GetComponent<PetController>().enabled = true;
        GetComponent<NeedsController>().enabled = true;
    }

    private void Update()
    {
        CheckHorizontalMovement();
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Jump();
        }
    }

    private void Jump()
    {
        if (!grounded) return;
        grounded = false;
        r2d.AddForce(new Vector2(0, jumpSpeed * 10000 * Time.deltaTime));
    }

    private void CheckHorizontalMovement()
    {
        if (Input.GetAxis("Horizontal") != 0)
        {
            r2d.AddForce(new Vector2(speed * 10000 * Time.deltaTime * Input.GetAxis("Horizontal"), 0));
        }
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.collider.CompareTag("Ground") &&
            collision.transform.position.y + 1.5f < transform.position.y)
        {
            grounded = true;
        }
    }

    private void OnCollisionExit2D(Collision2D collision)
    {
        if (collision.collider.CompareTag("Ground"))
        {
            grounded = false;
        }
    }
}
