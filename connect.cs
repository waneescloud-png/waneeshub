using HITR_API.models;
using Microsoft.AspNetCore.Mvc;
using System.Data.SqlClient;



// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace HITR_API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class connect : ControllerBase
    {
        private readonly string _connectToDB;
  
    public connect()
        {
            _connectToDB = connectdb.GetConnectString();
        }
        [HttpGet("ConnectToDB")]
        public IActionResult Get()
        {
            try
            {

                SqlConnection cnn = new SqlConnection(_connectToDB);
               cnn.Open();
                if(cnn.State==System.Data.ConnectionState.Open)
               return Ok(true);
                else
                {
                    return NotFound(false);
                }
            }
            catch(Exception ex)
            {
                return BadRequest(ex.Message);
            }
        }
       
    }
}
